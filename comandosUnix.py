'''COMANDOS UNIX:'''

~ #home
pwd #priting work diretory
ls #lista arquivos e pastas contidos no diretório de trabalho
	ls -a #inclusive arquivos ocultos
cd 'pasta' #entra na pasta (se ela estiver cintida no diretório de trabalho)
.. #um nível acima
../.. #dois níveis acima
echo 'algo' #imprime algo
mkdir 'pasta' #make diretory
cp file.txt /home/pasta/file.txt #copia o arquivo file.txt para a pasta
mv file.txt /home/pasta/file.txt #move o arquivo file.txt para a pasta
	mv file.txt life.txt #renomeia o arquivo file.txt para life.txt
rm #remove
	rm -r 'pasta' #remove pasta
rmdir 'pasta' #remove pasta se estiver vazia
cat file.txt #exibe o conteúdo do arquivo file.txt
clear (ou ctrl l) #limpa o terminal

'''COMANDOS GIT'''


git init #passa a versionar a pasta atual
git status #status dos arquivos na pasta
git add 'arquivo' #põe o arquivo na área de preparação (stage area)
	git add . #põe na área de preparação todos os arquivos da pasta de trabalho
git commit -m 'mensagem' #põe arquivos da área de preparação para o repositório (commit area)
git checkout #discarta mudanças em arquivos comitados no diretório de trabalho
git reset #tira arquivos da área de preparação