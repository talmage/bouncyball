def bounce():
    global x
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
    for j in range(141):
        l = 140 - j
        x = l + (radius + 1)
        LCD1IN8.draw_circle(x + 1,
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
        LCD1IN8.LCD_DisplayWindows(x - radius - 1, y - 1 - radius, x + 1 + radius, y + radius)
def setup():
    global l, k, radius, y
    LCD1IN8.LCD_Init()
    LCD1IN8.LCD_Clear()
    LCD1IN8.LCD_SetBL(123)
    l = 0
    k = 0
    radius = 10
    y = 64
k = 0
l = 0
y = 0
radius = 0
x = 0
setup()

def on_forever():
    bounce()
basic.forever(on_forever)
