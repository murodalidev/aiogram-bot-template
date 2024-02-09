import asyncio
import logging
import sys
from loader import dp, bot
from utils.notify_admins import on_startup_notify


async def main() -> None:
    await on_startup_notify()
    await dp.start_polling(bot)


if __name__ == "__main__":
    import handlers
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
