x = 0
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
radius = 10
y = 64
for i in range(141):
    x = i + (radius + 1)
    LCD1IN8.draw_circle(x - 1,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.WHITE),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.draw_circle(x,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.RED),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1)
    LCD1IN8.LCD_DisplayWindows(x - 1 - (radius + 1), y - 1 - radius, x + radius, y + radius)