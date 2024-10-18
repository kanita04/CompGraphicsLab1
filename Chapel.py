import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 400)
context = cairo.Context(surface)
context.paint()
