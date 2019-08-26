with open('index.html', 'w') as f:
    f.write('''
    <style>
    td {
        text-align: center;
        line-height: 2em;
        height: 2em;
        width: 2em;
    }

    table {
        transform: rotate(0deg);
        animation-duration: 10s;
        animation-name: spin;
        animation-iteration-count: infinite;
    }

    img {
        border-bottom: 5px solid pink;
        border-left: 5px solid pink;
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
    for A in range(-1, 10):
        if A == -1:
            f.write('<tr>')
            f.write('<td></td>')
            for B in range(10):
                f.write('<td>%d</td>' % B)
            f.write('</tr>')
            continue
        f.write('<tr>')
        for B in range(-1, 10):
            if B == -1:
                f.write('<td>%d</td>' % A)
                continue
            f.write('<td><img src="out/out-%d-%d-N.png"/></td>' % (A, B))
        f.write('</tr>')
    f.write('''</table>''')
