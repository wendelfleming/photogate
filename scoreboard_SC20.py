#!/usr/bin/env python3
import urwid

def exit_on_q(key):
    if key in ('esc'):
        raise urwid.ExitMainLoop()

screen = urwid.raw_display.Screen()
screen_cols, screen_rows = screen.get_cols_rows()

w_divider = urwid.Divider()
w_footer = urwid.Text('Press esc to exit.')

w_track_rows = int((screen_rows - 4 - 1)/2)

track1_speed = 1.2345678
track1_highest_speed = track1_speed
track2_speed = 2.3456789
track2_highest_speed = track2_speed

w_speed1 = urwid.BigText('{:01.2f}'.format(track1_speed), urwid.Thin6x6Font())
w_speed2 = urwid.BigText('{:01.2f}'.format(track2_speed), urwid.Thin6x6Font())

w_edit = urwid.Edit('', '0.0000')
urwid.AttrWrap(w_edit,'edit')

w_track1_body = urwid.Padding(w_speed1, 'center', None)
w_track1_body = urwid.Filler(w_track1_body, 'middle')
w_track1_header = urwid.Text('Highest Speed: {:01.2f} m/s '.format(track1_highest_speed), align='right') 
w_track1 = urwid.Frame(w_track1_body, header=w_track1_header)
w_track1 = urwid.LineBox(w_track1)
w_track1 = urwid.AttrWrap(w_track1, 'line')
w_track1 = urwid.BoxAdapter(w_track1, w_track_rows)

w_track2_body = urwid.Padding(w_speed2, 'center', None)
w_track2_body = urwid.Filler(w_track2_body, 'middle')
w_track2_header = urwid.Text('Highest Speed: {:01.2f} m/s '.format(track2_highest_speed), align='right') 
w_track2 = urwid.Frame(w_track2_body, header=w_track2_header)
w_track2 = urwid.LineBox(w_track2)
w_track2 = urwid.AttrWrap(w_track2, 'line')
w_track2 = urwid.BoxAdapter(w_track2, w_track_rows)

def set_track1_highest_speed(speed):
    global track1_highest_speed
    if speed > track1_highest_speed:
        track1_highest_speed = speed
        w_track1_header.set_text('Highest Speed: {:01.2f} m/s '.format(speed))

def set_track2_highest_speed(speed):
    global track2_highest_speed
    if speed > track2_highest_speed:
        track2_highest_speed = speed
        w_track2_header.set_text('Highest Speed: {:01.2f} m/s '.format(speed))

def set_new_speed(widget, text):
    speed = float(text)
    w_speed1.set_text('{:01.2f}'.format(speed))
    set_track1_highest_speed(speed)
    w_speed2.set_text('{:01.2f}'.format(speed))
    set_track2_highest_speed(speed)

urwid.connect_signal(w_edit, 'change', set_new_speed)

widget = urwid.Pile([w_edit, urwid.Text('Track 1 (m/s)'), w_track1, w_divider, urwid.Text('Track 2 (m/s)'), w_track2])
widget = urwid.Filler(widget, 'middle')
widget = urwid.Frame(widget, footer=w_footer)

loop = urwid.MainLoop(widget, screen=screen, unhandled_input=exit_on_q)
loop.run()
