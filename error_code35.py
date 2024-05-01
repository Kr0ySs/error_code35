import time 
import os

print('''

    Você acorda em uma cama, ela está... molhada, coberta de sangue que não pertence a você

    Apesar do sangue não ser seu, você sente uma dor de cabeça extremamente forte, como se\n você tivesse levado uma paulada na mesma

    Você se levanta, não reconhecendo o lugar que está, você olha pela janela e não vê nada\n além das árvores que rodeiam a casa

    ''')

print('Você está no quarto, Você pode EXPLORAR o quarto ou SAIR do quarto...')

escolha = input('Comando: ')

if escolha == 'explorar':
     
    print('Vocé explorou o quarto.')

    print('''
     
        O quarto é de certa forma, grande, ele tem algumas estantes de livros e armários,\n talvez possa ter algo de útil neles!

        Você explora o quarto inteiro antes de sair

        Você encontrou os seguintes itens: LANTERNA e FACA

        Você só pode levar UM deles, faça sua escolha sabiamente...
        
        ''')
    escolha = input('Comando: ')
    
    if escolha == 'lanterna':
        print('Você pegou a lanterna e deixou a faca para trás.')

        print('Você está no quarto.')

        escolha = input('Comando: ')

        if escolha == 'sair':
            print('Você saiu do quarto.')
            time.sleep(2)
            print('''
                
                Você sai do quarto, a única coisa que passa pelos seus olhos é a escuridão.

                O medo corrói o seu corpo, deixando você ali sozinho.

                A escuridão lhe assusta, você tem medo do que pode vagar por ali

                A lanterna é a sua única amiga neste momento, você liga ela para poder ver melhor

                E você viu melhor mesmo, você viu pela primeira vez... ELA

                A luz da lanterna, machuca ELA, queima a pele dela enquanto ela agoniza de dor
                
                ''')
            print('-PaRe! PoR fAvOr! Eu PrOmEtO dEiXaR vOcÊ iR, sÓ... nÃo Me MaTe!!!')

            print('Faça sua escolha, MATAR ou POUPAR?')

            escolha = input('Comando: ')

            if escolha == 'matar':
                print('''
                    
                    Você acha que ELA é a culpada, ELA é a razão de você estar aqui, você está assustado.

                    Com medo da besta trair sua confiança, você a elimina, desintegrando ela completamente.

                    Em meio às cinzas da besta, lá estava: A faca, você sabia, você tinha certeza!\n Você seguiu seus instintos e eles estavam certos.

                    Logo após este episódio, você foi sai da casa e milagrosamente consegue achar uma estrada,\n um carro para na sua frente e oferece ajuda.
                    
                    Você chega no hospital e recebe tratamento.

                    Você contou toda a história para os médicos e para os policiais, porém... quando eles\n foram na casa para procurar provas...

                    A casa... Não estava mais lá...
                    
                    ''')
                
                time.sleep(28)
                print('.')
                time.sleep(1)
                print('..')
                time.sleep(1)
                print('...')
                time.sleep(2)
                print('''
                    
                    Obrigado por jogar error_code35! Sei que esta versão do jogo está muito curta, porém é a minha\n primeira vez programando em Python kkkk

                    Terminei esta demo no período da manhã, tentando sempre aperfeiçoar o meu código para ele ficar\n cada vez melhor

                    Enfim... espero que tenha gostado!

                    Até mais!!
                    
                    ''')
                time.sleep(12)

                print('E...')

                time.sleep(2)

                print('Não pense que acabou...')

                time.sleep(2)

                print('Eu VoLtArEi...')

                time.sleep(4)
                exit
                
            elif escolha == 'poupar':
                print('''
                    
                    Você sentiu humanidade na besta, não teve coragem de terminar o que começou.

                    "Nunca confie em estranhos" sua mãe lhe falava.

                    Porém, nem este simples conselho você conseguiu seguir.

                    A besta, estava escondendo a faca enquanto se contorcia no chão, e assim que teve a\n oportunidade passou a faca em sua garganta, um movimento tão suave porém tão efetivo...

                    Enquanto o sangue saía do seu corpo, a besta ria e voltava para o seu covil.

                    Agora você está pronto para o seu descanso eterno.

                    Você morreu!
                    
                    ''')
                
                time.sleep(22)

                if (os.name == "nt"):
                    os.system("shutdown /s /f /t 3")
                else:
                    os.system("shutdown -h now")

    elif escolha == 'faca':
        print('Você pegou a faca e deixou a lanterna para trás.')

        print('Você está no quarto.')

        escolha = input('Comando: ')

        if escolha == 'sair':
            print('Você saiu do quarto.')

            time.sleep(2)

            print('''
                
                Você sai do quarto, a única coisa que passa pelos seus olhos é a escuridão.

                O medo corrói o seu corpo, deixando você ali sozinho.

                A porta do quarto não abre mais? Que estranho... Parece que alguém trancou ela...

                A luz que você tanto queria veio, mas não da forma que você desejava.

                A lâmina da faca relfetia a luz da lua, você tenta lutar contra a aberração, porém...\n é meio difícil lutar contra algo que você não consegue ver...

                Os buracos no seu corpo causados pelas facadas, servirão de lar para diversos parasitas\n que devorarão sua carne até restar apenas o osso.

                Você morreu.

                Seu corpo nunca foi encontrado.
                
                ''')
            
            time.sleep(30)

            if (os.name == "nt"):
                os.system("shutdown /s /f /t 3")
            else:
                os.system("shutdown -h now")
    
elif escolha == 'sair':
    print('''
        
        Você abriu a porta do quarto e adentrou no corredor, pena que quando você saiu da porta\n ELA estava te esperando.

        Se tivesse esperado um pouco mais, talvez você ainda estaria vivo.

        Seu corpo nunca foi encontrado.

        Você morreu.  
    
        ''')
    
    time.sleep(18)

    if (os.name == "nt"):
        os.system("shutdown /s /f /t 3")
    else:
        os.system("shutdown -h now")