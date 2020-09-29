from browser import console, timer
import math
from . import base
from .rect import Rect

_PI = 3.1415926535


def line(surf, color, startpos, endpos, width=1):
    ctx = surf.context
    ctx.beginPath()
    ctx.strokeStyle = base.tuple_to_css_color(color)
    ctx.lineWidth = width
    ctx.moveTo(*startpos)
    ctx.lineTo(*endpos)
    ctx.stroke()

def aaline(surf, color, startpos, endpos, blend=1):
    line(surf, color, startpos, endpos)

def lines(surf, color, closed, points, width=1):
    ctx = surf.context
    ctx.beginPath()
    ctx.strokeStyle = base.tuple_to_css_color(color)
    ctx.lineWidth = width
    ctx.moveTo(*points[0])
    for i in range(1, len(points)):
        ctx.lineTo(*points[i])
    if closed:
        ctx.closePath()
    ctx.stroke()

def aalines(surf, color, closed, points, blend=1):
    lines(surf, color, closed, points)

def rect(surf, color, rect, width=0, border_radius=0):
    if width < 0:
        return  # Do nothing
    ctx = surf.context
    ctx.beginPath()
    if width == 0:
        ctx.fillStyle = base.tuple_to_css_color(color)
        ctx.fillRect(rect.left, rect.top, rect.width, rect.height)
    else:
        ctx.lineWidth = width
        ctx.strokeStyle = base.tuple_to_css_color(color)
        ctx.rect(rect.left, rect.top, rect.width, rect.height)
    ctx.stroke()

def polygon(surf, color, points, width=0):
    if width < 0:
        return  # Do nothing
    ctx = surf.context
    ctx.beginPath()
    if width == 0:
        ctx.fillStyle = base.tuple_to_css_color(color)
    else:
        ctx.strokeStyle = base.tuple_to_css_color(color)
        ctx.lineWidth = width
    ctx.moveTo(*points[0])
    for i in range(1, len(points)):
        ctx.lineTo(*points[i])
    ctx.closePath()
    if width == 0:
        ctx.fill()
    else:
        ctx.stroke()

def arc(surf, color, rect, start_angle, stop_angle, width=1):
    if width < 0:
        return  # Do nothing
    ctx = surf.context
    ctx.beginPath()
    if width == 0:
        ctx.fillStyle = base.tuple_to_css_color(color)
        ctx.ellipse(rect.centerx, rect.centery, rect.width/2, rect.height/2, 0,
                    start_angle, stop_angle)
        ctx.fill()
    else:
        ctx.lineWidth = width
        ctx.strokeStyle = base.tuple_to_css_color(color)
        ctx.ellipse(rect.centerx, rect.centery, rect.width/2, rect.height/2, 0,
                    start_angle, stop_angle)
        ctx.stroke()


def ellipse(surf, color, rect, width=0):
    arc(surf, color, rect, 0, 2*_PI, width)

def circle(surf, color, center, radius, width):
    ellipse(surf, color, Rect(center[0]-radius, center[1]-radius, radius*2, radius*2), width)

