from services.utils import PrintDataRepo
from db.db import get_db
import asyncio


async def main():
    db = await get_db()
    await db.connect()

    print_data_repo = PrintDataRepo(db=db)
    result = await print_data_repo.get_stats()
    for data in result:
        print(data)

    db = await get_db()
    await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
