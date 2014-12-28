# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import random

WIDTH=600
HEIGHT=400
BALL_RADIUS=20
PAD_WIDTH=8
PAD_HEIGHT=80
HALF_PAD_WIDTH=PAD_WIDTH/2
HALF_PAD_HEIGHT=PAD_HEIGHT/2
LEFT=False
RIGHT=True

ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[]
paddle1_pos=[HALF_PAD_WIDTH,HEIGHT/2]
paddle1_vel=0
paddle2_pos=[WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
paddle2_vel=0
score1=0
score2=0


def spawn_ball(direction):
    global ball_pos,ball_vel
    ball_pos=[WIDTH/2,HEIGHT/2]
    if(direction):
        ball_vel=[-1,0.5]
    else:
        ball_vel=[1,0.5]
    
#define event handlers

def draw(canvas):
    global score1,score2
    
    # draw gutters and mid line
    canvas.draw_line([WIDTH/2,0],[WIDTH/2,HEIGHT],1,"White")
    canvas.draw_line([PAD_WIDTH,0],[PAD_WIDTH,HEIGHT],1,"White")
    canvas.draw_line([WIDTH-PAD_WIDTH,0],[WIDTH-PAD_WIDTH,HEIGHT],1,"White")
    
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    if ball_pos[1]<BALL_RADIUS or ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[1]*=-1
        
    elif ball_pos[0]<PAD_WIDTH+BALL_RADIUS:
        ball_vel[0]*=1.5
        if ball_pos[1]>=paddle1_pos[1]-HALF_PAD_HEIGHT and ball_pos[1]<=paddle1_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0]*=-1
        else:
            score2+=1
            LEFT=False
            spawn_ball(LEFT)
        
    elif ball_pos[0]>WIDTH-PAD_WIDTH-BALL_RADIUS:
        ball_vel[0]*=1.5
        if ball_pos[1]>=paddle2_pos[1]-HALF_PAD_HEIGHT and ball_pos[1]<=paddle2_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0]*=-1
        else:
            score1+=1
            LEFT=True
            spawn_ball(LEFT)
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,"White","White")
    
    # update paddle's vertical position,keep paddle on the screen
    paddle1_pos[1]+=paddle1_vel
    paddle2_pos[1]+=paddle2_vel
    
    if(paddle1_pos[1]<HALF_PAD_HEIGHT or paddle1_pos[1]>HEIGHT-HALF_PAD_HEIGHT):
        paddle1_pos[1]-=paddle1_vel
        
    if(paddle2_pos[1]<HALF_PAD_HEIGHT or paddle2_pos[1]>HEIGHT-HALF_PAD_HEIGHT):
        paddle2_pos[1]-=paddle2_vel
    
    # draw paddles
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    
    # draw scores
    canvas.draw_text(str(score1),[200,100],50,"White")
    canvas.draw_text(str(score2),[370,100],50,"White")

def keydown(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-5
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-5
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=5
    
def keyup(key):
    global paddle1_vel,paddle2_vel
    paddle1_vel=0
    paddle2_vel=0
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

spawn_ball(LEFT)
# start frame
frame.start()
