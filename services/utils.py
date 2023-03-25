from databases import Database
from sqlalchemy import select, desc, delete
from typing import List
import requests
from bs4 import BeautifulSoup
from config import parse_url
from db.models import Population as population_table


class GetDataRepo:

    def __init__(self, db: Database = None):

        self.db: Database = db


    async def parse_table(self) -> List:

        html_doc = requests.get(parse_url)
        if html_doc.status_code == 200:
            soup = BeautifulSoup(html_doc.content, 'html.parser')
            table = soup.find('table', attrs={"class": ["wikitable", "sortable", "jquery-tablesorter"]})

            rows = table.find_all('tr')

            data_list = []
            for row in rows[3:]:
                cells_raw = row.find_all('td')
                cells = [cell.text.strip() for cell in cells_raw]
                data_dict = {"country": cells[0],
                             "numbers": int(cells[1].replace(",", "")),
                             }
                data_list.append(data_dict)
            return data_list

    async def write_down(self) -> str:

        data_list = await self.parse_table()
        await self.db.execute(delete(population_table))
        await self.db.execute(population_table.__table__.insert().values(data_list))
        return "success"


class PrintDataRepo:

    def __init__(self, db: Database = None):

        self.db: Database = db

    async def get_stats(self) -> List:

        result = []

        db_biggest_country = await self.db.fetch_one(select(population_table).order_by(\
                                   desc(population_table.numbers)).limit(1))
        db_smallest_country = await self.db.fetch_one(select(population_table).order_by(\
                                   population_table.numbers).limit(1))
        all_countries = await self.db.fetch_all(select(population_table))

        for country in all_countries:
            result.append(f"Country: {country.country}")
            result.append(f"Population: {country.numbers}")

        result.append(f"The biggest country is {db_biggest_country.country}")
        result.append(f"Its population is {db_biggest_country.numbers}")

        result.append(f"The smallest country is {db_smallest_country.country}")
        result.append(f"It's population is {db_smallest_country.numbers}")

        return result
