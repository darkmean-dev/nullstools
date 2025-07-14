from nullstools import Mod

mod = Mod(
    title="Название",
    description="Описание"
)

mod.ru.add_object(
    TID="TID_TEST_NAME",
    RU="Привет!"
)

mod.build("mod.json")