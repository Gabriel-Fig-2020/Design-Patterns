# Design-Patterns
Esses são os projetos que são criado no curso https://www.udemy.com/course/padroes-de-projeto-com-python/.
Excelente curso para quem quer iniciar os estudos em padrões de projetos com a linguagem python.
## 1. Singleton (criação)
Usamos o padrão singleton em casos como logging (logs) ou operações de bancos de dados, spoolers de impressão e muitos outros cenários em que seja necessário que haja apenas uma única instância de determinado objeto disponível para toda a aplicação. Isso para evitar requisições conflitantes para o mesmo recurso.

## 2. Factory (criação)
É uma classe que cria objetos de diferentes tipos, por isso o nome factory (Fábrica). No projeto tem várias classes, invés de usar as classes, usamos uma factory que instância e retorna os objetos.
Qual a vantagem?
- Baixo acomplamento
- Apenas interface
- Reutilizar objetos

## 3 .  Facade (estrutura)
É um padrão estrutural, combina classes e objetos para compor estruturas maiores.
Basicamente é uma classe que instância outras classes, abstraindo o cliente de instanciar várias, a classe facade/faxada faz isso. Exemplo: funciona como uma organizadora de casamentos, você só contrata e a empresa se vira com tudo.
Cliente -> Facade --> chama e instancia todos os objetos/métodos que desejar
4. Proxy (estrutura)
É um padrão que serve de intermediação entre aplicações. Por exemplo o servidor Proxy (load balance, nginx,
No contexto de O.O. é uma classe que atua como interface para objetos (conexoes de rede, arquivos, etc...)

## 5. Observer (comportamento)
É um padrão de projeto de comportamento que temos observadores que recebem notificações quando algo acontece em outra classe.
O django usa algo semelhante ao implementar signals
6. command  (comportamento) - estudar mais a fundo
wizard implementa esse padrão
Desempenho de operações em fila

## 7. Template Method (comportamento) 
É semelhante a interface do solid, criamos uma classe abstrata que define os métodos que as filhas devem implementar e definimos o método que realiza as ações que todas as classes filhas devem usar (template method), que chama todas os outros métodos.
