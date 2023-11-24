"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass
def create_button(link, text, img):
    return rx.link(
        rx.hstack(
            rx.image(
                src=img,
                width="30px"
            ),
            rx.text(text,
                    font_size="20px",
                    font_weight="500",
                    font_family="DM Sans",
                    text_align="center",
                    color='#57618A',
                    width="calc(100% - 80px)"
                    ),
            padding="9px 7px",
            width="95vw",
            max_width="700px",
            border="1px solid rgb(128, 160, 201)",
            border_radius="5px",
            bg='white',
            box_shadow="rgb(128 160 201) 8px 8px 0px 0px",

            _hover={
                "cursor": "pointer",
                "translate": "4px 4px",
                "box shadow": "rgb(128 160 201) 4px 4px Opx Opx"
            }

        ),
        href=link,
        _hover={}
    )

def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                            rx.vstack(
                                rx.image(
                                    src='space_cat.JPG',
                                    width="168px",
                                    height="168px",
                                    border_radius="50%",
                                    margin_bottom="8px"
                                ),
                                rx.text(
                                    "Space Cat",
                                    font_weight="700",
                                    font_size="36px",
                                    line_height='1.5em',
                                    font_family="DM Sans",
                                    text_align="center",
                                    width="100%",
                                    color="rgb(255, 255, 255)",
                                    padding_bottom='3px'
                                ),
                                rx.text(
                                    "Awwsome ^^",
                                    font_weight="500",
                                    font_size="18px",
                                    line_height='1.5em',
                                    font_family="DM Sans",
                                    text_align="center",
                                    width="100%",
                                    color="rgb(255, 255, 255)",
                                    padding_bottom='30px'
                                ),

                                spacing="0"
                            ),
                rx.vstack(
                    create_button('https://youtu.be/uD4izuDMUQA?feature=shared', "hello, human!", "earth.png"),
                    create_button('https://www.youtube.com/watch?v=dQw4w9WgXcQ', "space travel", "another_planet.png"),
                    spacing="0.9em"
                ),
                ),
            padding_top="36px",
            width="100vw",
        ),

        bg = "linear-gradient(160deg, rgba(103, 151, 193,255),rgba(225, 156, 162, 255))",
        width = "100vw",
        height = "100vw"
    )

app = rx.App(stylesheets=["https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;500;600;700&display=swap"])
app.add_page(index)
app.compile()
