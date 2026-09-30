import os, re

cal_style = '''
    /* Calendar Specific Styles */
    .cal-day {
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .cal-day:hover:not(.disabled):not(.booked) {
      background-color: #C4975A;
      color: #fff;
    }
    .cal-day.selected {
      background-color: #242320 !important;
      color: #fff !important;
      font-weight: 700;
    }
    .cal-day.range {
      background-color: #EFECE6;
      color: #242320;
    }
    .cal-day.booked {
      background-color: #FEE2E2 !important;
      color: #EF4444 !important;
      cursor: not-allowed;
      text-decoration: line-through;
    }
    .cal-day.disabled {
      color: #D1D5DB;
      cursor: not-allowed;
    }
'''

def apply_style(p):
    if not os.path.exists(p): return
    with open(p, 'r', encoding='utf-8') as f: html = f.read()
    if '.cal-day.selected' not in html:
        # insert before </style>
        html = html.replace('</style>', cal_style + '\n  </style>')
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
        print("Patched style in", p)

apply_style('templates/01-stay/index.html')
for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    apply_style(os.path.join('Customer', d, 'index.html'))
