"""
Enter all inputs and outputs on a single line, separated by spaces.
Example:

The system uses a matrix with inputs 1, 2, and 3, and outputs 1 and 2.

Inputs:
1 2 3
Outputs:
1 2 

In the case of Kramer matrices with audio extraction,
it is necessary to specify which audio outputs are being used.
"""

msgs = []

print('Select matrix: \n1-Absolute\n2-Kramer')

matrix_type = int(input())

if matrix_type == 1:
    
    print("Outputs: ")
    outs = input()

    for i in outs.split(' '):

        switch_video = "> SWT #: " + i + "\\x0D\\x0A"
        switch_audio = "> SWA #: " + i + "\\x0D\\x0A"  #It seems the audio message is not needed to be sent separatedly anymore on new absolute devices
        msgs.append(switch_video)
        msgs.append(switch_audio)

elif matrix_type == 2:
    
    aux = []
    video = []
    audio = []

    print("Inputs: ")
    ins = input().split()
    print("Outputs: ")
    outs = input().split()
    print("Audio outputs: ")
    audio_outs = input().split()

    for in_i in ins:
        for out_i in outs:

                msg = "#AV " + in_i + ">" + out_i + "\\x0D "
                aux.append(msg)
                aux_string = ''.join(aux)

        video.append(aux_string)
        aux = []

    for in_i in ins:
        for audio_out_i in audio_outs:

                msg = "#AUD " + in_i + ">" + str(int(audio_out_i) + 8) + "\\x0D "
                aux.append(msg)
                aux_string = ''.join(aux)

        audio.append(aux_string)
        aux = []
    
    for i in range(len(video)):

        msg = video[i] + audio[i]
        msgs.append(msg)


else:
    print("Error")


for msg in msgs:
    print(msg)





