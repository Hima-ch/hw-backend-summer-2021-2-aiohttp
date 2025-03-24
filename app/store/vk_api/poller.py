import asyncio
from asyncio import Task

from app.store import Store


class Poller:
    def __init__(self, store: Store) -> None:
        self.store = store
        self.is_running = False
        self.poll_task: Task | None = None

    async def start(self) -> None:
        # TODO: добавить asyncio Task на запуск poll
        self.poll_task = asyncio.create_task(self.poll())

    async def stop(self) -> None:
        # TODO: gracefully завершить Poller
        if self.poll_task:
            self.poll_task.cancel()
            await self.poll_task


    async def poll(self) -> None:
        while True:
            updates = await self.store.vk_api.poll()
            await self.store.bots_manager.handle_updates(updates)
            await asyncio.sleep(1)
