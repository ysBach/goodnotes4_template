"""
Created by ysBach
2017-12-21
"""

from matplotlib import pyplot as plt
import matplotlib as mpl

import goodnotes4_template.core as gc

# =============================================================================
# Parameters
# =============================================================================
OUTPUT = 'Yellow_A4' # filename


# PAPER TYPE
PAPER_TYPE = 'A' # A or B
PAPER_SIZE = 4   # Usually 0 ~ 10
PAPER_MARGIN = [0, 0, 1, 0.95]
# [left, bottom, right, top] in normalized (0, 1) figure coordinates.
FACECOLOR = (250/255, 242/255, 173/255)
# Yellow = (250/255, 242/255, 173/255)
# White = 'w'
# etc


# MAIN RULE/LINE
NLINE = 32 # 32 for A4

# --- Main rules
RULE_COLOR = (0, 0.5, 0.5)
RULE_ALPHA = 1
RULE_LW = 0.3
RULE_LS = '-'

# --- The top rule
TOPRULE_COLOR = 'k'
TOPRULE_ALPHA = 1
TOPRULE_LW = 1
TOPRULE_LS = '-'

# --- Vertical guiding lines
GUIDE_COLOR = 'r'
GUIDE_ALPHA = 1
GUIDE_LW = 0.2
GUIDE_LS = '-' 
GUIDE_X = [14.5, 15]

# --- Vertical middle line
MID_COLOR = 'k'
MID_ALPHA = 0.15
MID_LW = 0.2
MID_LS = '-'


# X/Y AXES SETTING
XYFRAME_ON = False

TICK_TOP = False
TICKLABEL_TOP = False
TICK_BOTTOM = False
TICKLABEL_BOTTOM = False
TICK_LEFT = False
TICKLABEL_LEFT = True
TICK_RIGHT = False
TICKLABEL_RIGHT = True

# --- labels min/max: works only if some of the above are ``True``
XAXIS_MIN = 0
XAXIS_MAX = 100
YAXIS_MIN = 0
YAXIS_MAX = NLINE + 1 # Best to set ``NLINE + 1``

# --- labels fonts: works only if some of the above are ``True``
XTICK_LABELSIZE = 4
YTICK_LABELSIZE = 4
XTICK_COLOR     = 'grey'
YTICK_COLOR     = 'grey'


# Page/Date
PUT_PAGE_DATES = True
PAGE_X = 60
PAGE_Y = -0.2
PAGE_COLOR = 'grey'
PAGE_FONTSIZE = 8
DATE_X = 80
DATE_Y = -0.2
DATE_COLOR = 'grey'
DATE_FONTSIZE = 8


#%%
# =============================================================================
# Definitions
# =============================================================================
mpl.rcParams['xtick.labelsize'] = XTICK_LABELSIZE
mpl.rcParams['ytick.labelsize'] = YTICK_LABELSIZE
mpl.rcParams['xtick.color'] = XTICK_COLOR
mpl.rcParams['ytick.color'] = YTICK_COLOR

def DRAW_LINES(ax):
    ax.axhline(y=0, color=TOPRULE_COLOR, alpha=TOPRULE_ALPHA, lw=TOPRULE_LW, 
               ls=TOPRULE_LS)
    for i in range(NLINE):
        ax.axhline(y=i+1, color=RULE_COLOR, alpha=RULE_ALPHA, lw=RULE_LW,
                   ls=RULE_LS) 
    
    for x in GUIDE_X:
        ax.axvline(x=x, ymin=1/YAXIS_MAX, ymax=1, color=GUIDE_COLOR, 
                   alpha=GUIDE_ALPHA, lw=GUIDE_LW, ls=GUIDE_LS)    
    mid_x = ((XAXIS_MAX - XAXIS_MIN) - max(GUIDE_X))/2 + max(GUIDE_X)
    ax.axvline(x=mid_x, ymin=1/YAXIS_MAX, ymax=1, color=MID_COLOR, 
               alpha=MID_ALPHA, lw=MID_LW, ls=MID_LS)
    
#%%
# =============================================================================
# Main Part
# =============================================================================
figsize = gc.figure_size()
fig = plt.figure(figsize=figsize)
ax = fig.add_subplot(1,1,1)

# Set face color
ax.set_facecolor(FACECOLOR)

# Set frame
ax.set_xlim(XAXIS_MIN, XAXIS_MAX)
ax.set_ylim(YAXIS_MIN, YAXIS_MAX)
ax.set_frame_on(XYFRAME_ON)

# Draw main rules
DRAW_LINES(ax)

# Put page and date
if PUT_PAGE_DATES:
    ax.text(PAGE_X, PAGE_Y, 'Page', color=PAGE_COLOR, fontsize=PAGE_FONTSIZE)
    ax.text(DATE_X, DATE_Y, 'Date', color=DATE_COLOR, fontsize=DATE_FONTSIZE)

# Set tick parameters
ax.tick_params(top=TICK_TOP, bottom=TICK_BOTTOM,
               left=TICK_LEFT, right=TICK_RIGHT,
               labeltop=TICKLABEL_TOP, labelbottom=TICKLABEL_BOTTOM, 
               labelleft=TICKLABEL_LEFT, labelright=TICKLABEL_RIGHT)

# Set final layout
plt.gca().invert_yaxis()
plt.tight_layout(rect=PAPER_MARGIN)

# save
plt.savefig(OUTPUT+'.pdf', facecolor=ax.get_facecolor(), edgecolor='none')

# close interactive window
plt.close(fig)