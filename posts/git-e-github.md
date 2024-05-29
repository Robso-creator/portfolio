# Git e Github

Versionamento de código é um dos principais pilares quando falamos sobre programação. Deixar seus projetos salvos no seu computador é como atirar uma flecha para cima e torcer para não acertar o próprio pé! Você, Junior, precisa defender isso com todas as fibras do seu ser, a fim de não se tornar um Sênior que deixa scripts importantes para a empresa na pasta "Documentos" do computador.

## Mas afinal, o que é Git?

Entender o que ele é vai facilitar a utilização da ferramenta de forma efetiva no seu dia a dia, seja no trabalho ou em projetos pessoais. O Git é uma das diversas ferramentas de versionamento de código disponíveis no mercado. Outros exemplos incluem CVS, Perforce, Subversion, e por aí vai. A principal diferença entre o Git e as outras ferramentas está na forma como enxergam os dados. Enquanto os concorrentes comumente funcionam como um "controle de versão baseado em delta/diferenças (delta-based)", onde a informação é armazenada como uma lista das alterações feitas nos arquivos, o Git tira uma foto de como todos os arquivos estão e os salva em "snapshots" toda vez que você realiza alguma alteração. Para evitar trabalho desnecessário, isso só acontece se de fato existir alguma mudança nos arquivos.

No fim do dia, todos servem para o mesmo propósito: garantir controle sobre nossos códigos de forma histórica, possibilitando retornar a um estado anterior caso alguma das nossas mudanças crie algum tipo de caos dentro das aplicações. Além disso, permite comparar versões, enxergar falhas e identificar oportunidades de melhoria.

O mais interessante do Git é o fato de ter sido criado pelo mesmo homem que desenvolveu o Linux! Sabe o que isso significa? Ele é na faixa, totalmente [open source](https://www.redhat.com/pt-br/topics/open-source/what-is-open-source).

## Principais conceitos do Git

**Repositório (Repository):**
Um repositório, no contexto do Git, é o local onde as diferentes versões de um projeto são armazenadas. Pode ser tanto local, ou seja, no seu próprio computador, quanto remoto, hospedado em um servidor acessível pela internet.

**Commit:**
Um commit representa uma versão específica do projeto. Ele contém um conjunto de alterações feitas nos arquivos, marcando um ponto importante na história do desenvolvimento.

**Branch:**
Um branch é uma ramificação independente de desenvolvimento que possibilita trabalhar em funcionalidades ou correções de bugs de forma separada. Cada branch tem sua própria linha de desenvolvimento, o que permite uma abordagem organizada para o desenvolvimento de novos recursos.

**Merge:**
O merge é o processo de combinar as alterações de um branch em outro. Isso é especialmente útil para integrar uma funcionalidade desenvolvida em um branch de feature de volta ao branch principal do projeto.

**Conflito:**
Um conflito ocorre quando o Git encontra alterações conflitantes no mesmo trecho de código durante uma operação de merge. Nestes casos, é necessário resolver esses conflitos manualmente, garantindo uma integração adequada das alterações.

**Stash:**
O stash é uma funcionalidade que permite "guardar" temporariamente alterações que ainda não estão prontas para serem commitadas. Isso facilita a mudança de branch sem perder o trabalho em andamento.

**Pull Request:**
Um Pull Request é uma solicitação feita em plataformas como o GitHub para integrar as alterações de um branch em outro. Esta é uma forma essencial de colaboração e revisão de código em projetos colaborativos.

**Tag:**
Uma tag é uma marcação específica em um commit que indica um ponto de referência importante, como uma versão de release. Ela é útil para identificar e marcar versões específicas do projeto.

**Clone:**
O clone é o processo de criar uma cópia local de um repositório Git já existente. Isso possibilita trabalhar com o código em seu ambiente de desenvolvimento local.

**Fork:**
Um fork é uma cópia independente de um repositório, frequentemente usado em projetos de código aberto. Isso permite contribuições sem a necessidade de permissões de gravação no repositório original.

**Rebase:**
O rebase é uma operação que permite reorganizar o histórico de commits, alterando a ordem ou incorporando as alterações de um branch em outro de forma mais linear.

**.gitignore:**
O arquivo .gitignore contém uma lista de padrões que indica ao Git quais arquivos e pastas devem ser ignorados ao rastrear alterações. É útil para evitar a inclusão de arquivos desnecessários, como configurações locais ou logs, no controle de versão.

## Principais comandos do Git

O Git é uma ferramenta robusta, com INÚMEROS comandos para auxiliar os desenvolvedores nos desafios do versionamento de código. No entanto, separei os 11 comandos principais que, com conhecimento de causa, acredito serem os mais importantes para um Júnior conhecer:

## 1. [Git Init](https://git-scm.com/docs/git-init/pt_BR)

<pre><code>git init</code></pre>

Inicializa um novo repositório Git em um diretório local. Este comando cria um novo repositório Git vazio ou transforma um diretório existente em um repositório Git.

## 2. [Git Clone](https://git-scm.com/docs/git-clone/pt_BR)

<pre><code>git clone \\repositorio-a-copiar// </code></pre>

Clona um repositório Git existente de um repositório remoto (como GitHub, GitLab, etc.) para o seu sistema local. Isso cria uma cópia local do repositório completo, incluindo todo o histórico de versões.

## 3. [Git Add](https://git-scm.com/docs/git-add/pt_BR)

<pre><code>
git add \\arquivo-adicionar//

# Você também pode colocar "." para adicionar todos os arquivos alterados
</code></pre>

Adiciona arquivos ou alterações específicas ao “staging area”, preparando-os para serem incluídos no próximo commit. Pode ser usado com nomes de arquivos ou wildcards(*.txt, file?.txt) para adicionar múltiplos arquivos de uma vez.

## 4. [Git Commit](https://git-scm.com/docs/git-commit/pt_BR)

<pre><code>git commit -m "consertei o bug do while infinito"</code></pre>

Grava as mudanças no repositório local, criando um novo instantâneo (snapshot) com uma mensagem descritiva. As alterações no “staging area” são incluídas no commit.

## 5. [Git Push](https://git-scm.com/docs/git-push/pt_BR)

<pre><code>git push origin master</code></pre>

Envia as alterações do repositório local para um repositório remoto, como o GitHub. Isso atualiza o repositório remoto com as últimas alterações.

## 6. [Git Pull](https://git-scm.com/docs/git-pull/pt_BR)

<pre><code>git push origin master</code></pre>

Obtém as últimas alterações de um repositório remoto e as mescla automaticamente com o repositório local. É usado para manter o repositório local atualizado com o repositório remoto.

## 7. [Git Branch](https://git-scm.com/docs/git-branch/pt_BR)

<pre><code>
git branch # Lista todos as branches existentes

git branch \\nome-branch// # Cria uma branch nova
</code></pre>

Cria, lista ou exclui branches. Branches são ramificações independentes do desenvolvimento que permitem trabalhar em funcionalidades separadas sem interferir no código principal.

## 8. [Git Checkout](https://git-scm.com/docs/git-checkout/pt_BR)

<pre><code>
git checkout \\nome-branch// # Muda para uma branch existente

git checkout -b \\nome-branch// # Cria uma branch nova e muda para a mesma
</code></pre>

Permite alternar entre diferentes branches ou restaurar arquivos individuais de um commit anterior. Também pode ser usado para criar novos branches a partir de commits existentes.

## 9. [Git Merge](https://git-scm.com/docs/git-merge/pt_BR)

<pre><code>git merge feature # Você está na branch "main" e irá mesclar a branch "feature" nela</code></pre>

Combina as alterações de um branch (ou de um commit específico) com o branch atual. Isso integra o trabalho de desenvolvimento feito em diferentes branches.

## 10. [Git Status](https://git-scm.com/docs/git-status/pt_BR)

<pre><code>git status</code></pre>

Mostra o estado atual do repositório, incluindo quais arquivos foram modificados, quais estão no “staging area” e quais não estão sendo rastreados pelo Git.

## 11. [Git Log](https://git-scm.com/docs/git-log/pt_BR)

<pre><code>git log</code></pre>

Exibe um histórico detalhado dos commits, mostrando informações como o autor, data, mensagem e identificador único de cada commit.


## Os três estados

**Diretório de Trabalho (Working Directory):**
É o estado dos arquivos no seu sistema de arquivos local. Neste estado, os arquivos podem ser modificados, adicionados ou excluídos sem que o Git esteja ciente dessas mudanças.

**Área de Preparação (Staging Area ou Index):**
É o estado intermediário entre o diretório de trabalho e o repositório local. Aqui, você seleciona quais modificações serão incluídas no próximo commit. Os arquivos adicionados à staging area estão prontos para serem registrados como uma nova versão.

**Repositório Local:**
É o estado onde o Git armazena todas as versões registradas do seu projeto. Os arquivos no repositório local já foram confirmados (comitados) como parte da história do projeto. Eles podem ser recuperados em qualquer momento e compartilhados com outros membros da equipe.

Esses três estados refletem o fluxo de trabalho típico do Git. Você primeiro faz modificações nos arquivos no diretório de trabalho. Em seguida, adiciona as alterações relevantes à staging area para prepará-las para o próximo commit. Por fim, você faz um commit para registrar essas alterações no repositório local como uma nova versão.

## Onde entra o Github nisso?

O GitHub é uma plataforma baseada na nuvem que desempenha um papel crucial no mundo do desenvolvimento de software.
Ele serve como um ambiente de hospedagem e colaboração para projetos que utilizam o sistema de controle de versão Git.
É aqui que armazenamos nossos [repositórios](https://codigoparatodos.blog/2023/09/24/de-junior-para-junior-introducao-ao-git-e-github/#repositorio) remotos!

## Principais Características:

**Hospedagem de Repositórios Git:**
O GitHub oferece um local centralizado onde os desenvolvedores podem hospedar seus repositórios Git, tornando-os acessíveis a colaboradores de todo o mundo.

**Colaboração Distribuída:**
Permite que equipes trabalhem de forma colaborativa em projetos, independentemente da sua localização geográfica. Vários desenvolvedores podem contribuir simultaneamente para um projeto.

**Controle de Versão Eficiente:**
Facilita o controle de versão e o rastreamento das alterações feitas em um projeto. Cada commit é registrado, permitindo uma visão clara da evolução do código.

**Gestão de Issues e Pull Requests:**
Possibilita o acompanhamento de tarefas, bugs e melhorias por meio do sistema de issues. Os pull requests permitem que os desenvolvedores solicitem a integração de suas alterações no projeto principal.

**Ambiente de Desenvolvimento Integrado (IDE):**
O GitHub oferece um ambiente de desenvolvimento web chamado “GitHub Codespaces”, que permite aos desenvolvedores editar, compilar e depurar código diretamente no navegador.

**Integração com Ferramentas de Automação (CI/CD):**
Integra-se facilmente com diversas ferramentas de integração contínua/desdobramento contínuo (CI/CD), automatizando a construção, teste e implantação de projetos.

## Usos Comuns do GitHub:

**Projetos de Código Aberto:**
Muitos projetos de código aberto utilizam o GitHub para permitir contribuições da comunidade, além de fornecer um espaço centralizado para colaboradores.

**Desenvolvimento de Software Empresarial:**
Empresas usam o GitHub para gerenciar e colaborar em projetos de software internos, facilitando o trabalho em equipe e a manutenção do código.

**Portfólios de Desenvolvedores:**
Muitos desenvolvedores utilizam o GitHub para mostrar seus projetos e habilidades a potenciais empregadores ou colaboradores.

**Documentação Técnica:**
Além de código, o GitHub também é usado para hospedar documentação técnica e recursos educacionais.

O GitHub desempenha um papel fundamental no ecossistema de desenvolvimento de software, facilitando a colaboração, o controle de versão e a distribuição de projetos. Com uma ampla gama de recursos e uma comunidade ativa, é uma ferramenta indispensável para desenvolvedores de todos os níveis de experiência, nem Junior escapa.

### Links interessantes:

- [PDF com lista de comandos Git](https://education.github.com/git-cheat-sheet-education.pdf)
- [Fernanda Kipper | Aula sobre Git e Github](https://www.youtube.com/watch?v=pyM5QLS2h6M&pp=ygUDZ2l0)
- [Curso gratuito sobre Git e Github](https://www.dio.me/courses/introducao-ao-git-e-ao-github)
- [Documentação oficial do Git](https://git-scm.com/doc)
- [Documentação oficial do GitHub](https://docs.github.com/)

### Referências:

**Examples of wildcard characters**. Disponível em: https://support.microsoft.com/en-gb/office/examples-of-wildcard-characters-939e153f-bd30-47e4-a763-61897c87b3f4&gt;. Acesso em: 24 set. 2023.

**Git – git documentation**. Disponível em: https://git-scm.com/docs/git/pt_BR&gt;. Acesso em: 24 set. 2023.

**Git – what is git?**. Disponível em: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F&gt;. Acesso em: 24 set. 2023.

**O que é open source?**. Disponível em: https://www.redhat.com/pt-br/topics/open-source/what-is-open-source&gt;. Acesso em: 24 set. 2023.
