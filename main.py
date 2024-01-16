import pygame_gui
import pygame

class Menu:
    def __init__(self):
        self.Star()

    def Star(self):
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        color = 'white'
        background = pygame.Surface(size)
        background.fill(pygame.Color(color))
        manager = pygame_gui.UIManager(size)
        start = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 50), (100, 50)),
            text="Старт",
            manager=manager
        )
        option = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 150), (100, 50)),
            text="Настройки",
            manager=manager
        )

        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == start:
                            if color == "black":
                                color = 'white'
                            else:
                                color = "black"
                            background.fill(pygame.Color(color))
                        if event.ui_element == option:
                            pass
                manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()

    def Opt(self):
        pygame.init()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        screen.fill()

if __name__ == '__main__':
    Menu()