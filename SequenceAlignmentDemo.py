Label('Sequence Alignment #3', 200, 20, size=18, bold=True)

app.stepsPerSecond = 2
app.index = 0

app.similarityMatrix = {
  'A': {'A':  2, 'T':  1, 'G': -1, 'C': -1},
  'T': {'A':  1, 'T':  2, 'G': -1, 'C': -1},
  'G': {'A': -1, 'T': -1, 'G':  2, 'C':  1},
  'C': {'A': -1, 'T': -1, 'G':  1, 'C':  2}
}


# Not aligned sequences
X ='AGTAGACCACACATGGTGACAGC'
Y = 'GACGACTCATCCTGACAGC'
Y_aligned = '____GACGACTCATCCTGACAGC'



Label('Similarity count unaligned: ', 180, 100, size=20)
similarityCount = Label(0, 320, 100, size=20)
dna1 = Label(X, 90, 140, size=20, align='left', font='monospace')
dna2 = Label(Y, 90, 160, size=20, align='left', font='monospace')
highlight = Rect(90, 130, 12, 40, fill='green', opacity=50)

Label('Similarity count aligned: ', 180, 200, size=20)
similarityCount_aligned = Label(0, 320, 200, size=20)
dna1_aligned = Label(X, 90, 240, size=20, align='left', font='monospace')
dna2_aligned = Label(Y_aligned, 90, 260, size=20, align='left', font='monospace')
highlight_aligned = Rect(90, 230, 12, 40, fill='blue', opacity=50)

def onStep():
    highlight.left += 12
    highlight_aligned.left += 12
    
    # Get the bases, and see how much we should adjust the score.
    base1 = dna1.value[app.index]
    if (app.index < len(Y)-1): 
        base2 = dna2.value[app.index]
        similarityCount.value += app.similarityMatrix[base1][base2]
    
        # Change the highlight color.
        if (base1 == base2):
            highlight.fill = 'green'
        else:
            highlight.fill = 'red'
    else: #out of range for #2 
        similarityCount.value -= 1 #penalty of 1
        highlight.fill = 'red'
        
    aligned_base2 = dna2_aligned.value[app.index]
    if (aligned_base2 == '_'):
        highlight_aligned.fill = 'blue'
    else: 
        similarityCount_aligned.value += app.similarityMatrix[base1][aligned_base2]
    
        # Change the highlight color.
        if (base1 == aligned_base2):
            highlight_aligned.fill = 'green'
        else:
            highlight_aligned.fill = 'red'
        
    
    

    app.index += 1
    if (app.index == len(X)-1):
        app.stop()
