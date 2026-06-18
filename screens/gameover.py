import pygame

def draw_gameover(
    screen,
    font,
    width,
    height,
    game_state,
    score,
    highscore
):

    screen.fill((0, 0, 0))

    text = font.render(
        "YOU WIN" if game_state == "win" else "YOU DIED",
        True,
        (0, 255, 0) if game_state == "win" else (255, 0, 0)
    )

    final_score_text = font.render(
        f"Final Score: {score}",
        True,
        (255, 255, 255)
    )

    highscore_text = font.render(
        f"High Score: {highscore}",
        True,
        (255, 255, 255)
    )

    restart_text = font.render(
        "Press R to Restart",
        True,
        (255, 255, 255)
    )

    screen.blit(
        final_score_text,
        (
            width // 2 - final_score_text.get_width() // 2,
            height // 2 - 20
        )
    )

    screen.blit(
        highscore_text,
        (
            width // 2 - highscore_text.get_width() // 2,
            height // 2 + 40
        )
    )

    screen.blit(
        text,
        (
            width // 2 - 60,
            height // 3
        )
    )

    screen.blit(
        restart_text,
        (
            width // 2 - 100,
            height // 2 + 100
        )
    )