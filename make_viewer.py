import string
classes = ''
classes += string.digits
classes += string.uppercase
classes += ''.join([c for c in string.lowercase if c not in 'cijklmopsuvwxyz'])

with open('index.html', 'w') as f:
    f.write('''
    <style>
    td {
        text-align: center;
        line-height: 2em;
        height: 2em;
        width: 2em;
    }

/*
    table {
        transform: rotate(0deg);
        animation-duration: 10s;
        animation-name: spin;
        animation-iteration-count: infinite;
    }
*/

    img:hover {
        transform: rotate(180deg);
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      10% { transform: rotate(180deg); }

      50% { transform: rotate(180deg); }
      60% { transform: rotate(0deg); }

    }
    </style>
    ''')

    f.write('''
    <table>
    ''')
    for A in range(-1, 36):
        if A == -1:
            f.write('<tr>')
            f.write('<td></td>')
            for B in range(36):
                f.write('<td>%s</td>' % classes[B])
            f.write('</tr>')
            continue
        f.write('<tr>')
        for B in range(-1, 36):
            if B == -1:
                f.write('<td>%s</td>' % classes[A])
                continue
            f.write('<td><img src="emout-reg/out-%d-%d.png"/></td>' % (A, B))
        f.write('</tr>')
    f.write('''</table>''')
