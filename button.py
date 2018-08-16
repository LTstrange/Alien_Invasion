import pygame.font


class Button:
    def __init__(self, ai_settngs, screen, msg):
        """init button attribute"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set button's size and other attribute
        self.width, self.height = 200, 50
        self.button_color = (200, 200, 200)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # create rect of button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 创建按钮标签，只需一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

