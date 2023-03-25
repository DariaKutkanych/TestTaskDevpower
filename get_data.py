from services.utils import GetDataRepo, PrintDataRepo
from db.db import get_db
from databases import Database
import asyncio

async def main():
    db = await get_db()
    await db.connect()

    get_data_repo = GetDataRepo(db=db)
    data = await get_data_repo.write_down()
    print(data)

    db = await get_db()
    await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())

