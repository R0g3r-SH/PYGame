def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Retorna una superficie con texto escrito encima """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ Un elemento de interfaz grafica para añadir. """

    def __init__(self, center_position, text, font_size, bg_rgb, inactive_rgb, active_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            inactive_rgb (text colour) - tuple (r, g, b)
            active_rgb (text colour) - tuple (r, g, b)
            action - el estado de cambio asociado a este boton
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=inactive_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=active_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # Asignar una accion al boton
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ 
            Actualiza la variable mouse_over y retorna la accion del boton al
            hacer click.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Dibuja un elemento sobre la superficie."""
        surface.blit(self.image, self.rect)
