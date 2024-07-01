from src.model.human import Human
from src.model.carrot import Carrot
from src.model.datamanager import DataManager
from src.controller.controller import App
from src.view.mainview import MainView

def main():
    data_manager = DataManager()
    controller = App()

    human = Human(id=1, position=(10, 110), size=(16, 16), name="John", age=30)
    # carrot = Carrot(id=2, position=(20, 20), size=(16, 16))

    data_manager.add_human(human)
    # data_manager.add_gatherable(carrot)


if __name__ == "__main__":
    main()
