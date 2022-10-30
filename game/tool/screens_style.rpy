define gui.userinfo_lateralframe_ysize = 600
define gui.lateralframescroll_ysize = 520
style menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform close_zoom:
        xanchor 25
        size (75, 25)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform close_zoom_mobile:
        xanchor 35
        size (105, 35)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
