function bounce () {
    for (let i = 0; i <= 140; i++) {
        x = i + (radius + 1)
        LCD1IN8.DrawCircle(
        x - 1,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.WHITE),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1
        )
        LCD1IN8.DrawCircle(
        x,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.RED),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1
        )
        LCD1IN8.LCD_DisplayWindows(
        x - 1 - (radius + 1),
        y - 1 - radius,
        x + radius,
        y + radius
        )
    }
    for (let j = 0; j <= 140; j++) {
        i = 140 - j
        x = i + (radius + 1)
        LCD1IN8.DrawCircle(
        x + 1,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.WHITE),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1
        )
        LCD1IN8.DrawCircle(
        x,
        y,
        radius,
        LCD1IN8.Get_Color(LCD_COLOR.RED),
        DRAW_FILL.DRAW_FULL,
        DOT_PIXEL.DOT_PIXEL_1
        )
        LCD1IN8.LCD_DisplayWindows(
        x - radius - 1,
        y - 1 - radius,
        x + 1 + radius,
        y + radius
        )
    }
}
function setup () {
    LCD1IN8.LCD_Init()
    LCD1IN8.LCD_Clear()
    LCD1IN8.LCD_SetBL(123)
    i = 0
    j = 0
    radius = 10
    y = 64
}
let j = 0
let i = 0
let y = 0
let radius = 0
let x = 0
setup()
basic.forever(function () {
    bounce()
})
