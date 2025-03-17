import pygame

def button(screen, font, x, y, width, height, text, on_click,color=(200, 200, 200), hover_color=(150, 150, 150), text_color=(0, 0, 0)):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, width, height)
    is_hovered = rect.collidepoint(mouse_pos)
    current_color = hover_color if is_hovered else color

    pygame.draw.rect(screen, current_color, rect)
    drawText(screen, font, text, x + width // 2, y + height // 2, text_color, center=True)

    if is_hovered and click[0]:  
        pygame.time.delay(150)  
        on_click()


def drawText(screen, font, text, x, y, color, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)