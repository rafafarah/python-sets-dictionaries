def test_extend_list():
    user_data_science = [15, 23, 43, 56]
    user_machine_learning = [13, 23, 56, 42]

    watched = []
    watched = user_data_science.copy()
    watched.extend(user_machine_learning)
    # final list has duplicated elements
    print(watched)

def test_set():
    user_data_science = {15, 23, 43, 56}
    user_machine_learning = {13, 23, 56, 42}
    # a set has no duplicated element
    # set has no index access/no order
    watched_union = user_machine_learning | user_data_science
    watched_intesec = user_machine_learning & user_data_science
    watched_diff = user_machine_learning - user_data_science
    watched_exclusive = user_machine_learning ^ user_data_science
    print(watched_exclusive)
    for user in watched_exclusive:
        print(user)

def test_modifying_set():
    user = {1, 5, 76, 34, 52, 13, 17}
    print(len(user))
    user.add(765)
    print(len(user))

    # frozenset is a not mutable set
    frozen = frozenset(user)
    print(frozen)

def test_dictionary():
    # creating dictionary from constructor, not usual
    # dic = dict(jorge = 1, doge = 2, name = 2, come = 1,)
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }

    # adding to dic
    dic["jefferson"] = 1
    print(dic)
    # removing from dic
    del dic["jefferson"]
    print(dic)

    print(dic["doge"])
    # set allows to define a default value if key isn't present
    print(dic.get("asfd", 0))

def test_iterate_dict():
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }
    # print dict keys
    for elem in dic:
        print(elem)
    print()
    # print dict values
    for elem in dic.values():
        print(elem)
    print()
    # print dict couple
    for elem in dic.items():
        print(elem)
    print()
    # print dict couple anpacked
    for key, value in dic.items():
        print(key, ":", value)

def test_defaultdict():
    text = "Welcome my name is Jorge I like names vey much and I have a dog and I like dog very much"
    text = text.lower()

    # building a dictionary from text
    dic = {}
    for word in text.split():
        dic[word] = dic.get(word, 0) + 1
    print(dic)
    print()
    from collections import defaultdict
    # use defaultdict with int to return 0 as default value
    dic_default = defaultdict(int)
    for word in text.split():
        dic_default[word] += 1
    print(dic_default)

def test_counter_dict():
    from collections import Counter
    text = "Welcome my name is Jorge I like names vey much and I have a dog and I like dog very much"
    text = text.lower()

    # use Counter direct with iterable
    dic_default = Counter(text.split())
    print(dic_default)

def test_collections():
    from collections import Counter
    text_flutter = """
Antes de entrarmos no t??pico sobre o Nuvigator propriamente dito, precisamos entender o que temos dispon??vel hoje nativamente no Flutter e como ?? criado para posteriormente notarmos quais s??o as diferen??as expressivas de um para o outro. Normalmente, tendemos a utilizar rotas como os sites utilizam, j?? que ?? um padr??o difundido h?? v??rios anos na web, mas, diferente dos sites que os usu??rios t??m acesso ?? URL, em Flutter utilizamos este artif??cio ???por baixo dos panos???.
Independentemente do que utilizamos para navegar, ?? importante entender que os usu??rios esperam conseguir ir de uma tela para a outra e voltar. Algumas vezes, precisaremos passar informa????es de uma tela para a tela seguinte que ser?? aberta (como os detalhes de um produto, por exemplo) ou mesmo passar dados de uma segunda tela para a anterior. Esse fluxo de ???vai e vem??? dos dados precisa ser tratado com bastante cuidado por n??s programadores e programadoras.
A documenta????o do Flutter traz algumas formas de criar a navega????o, sendo elas:
Cada uma dessas formas de navega????o tem suas particularidades, diferen??as, vantagens e desvantagens. Basicamente, o que precisamos entender agora ?? que cada uma dessas implementa????es ?? uma forma de empilhar, substituir e remover telas abertas ao longo da navega????o realizada pelos usu??rios.
Push e Pop
O mecanismo de pilha, ou seja, o primeiro que ?? aberto ?? o ??ltimo a ser fechado, ?? amplamente utilizado e difundido no universo Flutter. Al??m de ser a forma mais simples de navegar entre telas, segundo os pr??prios criadores do framework, os comandos push e pop s??o utilizados amplamente para realizar estas a????es. Podemos criar um exemplo b??sico seguindo a documenta????o do Flutter. A seguir, veja um exemplo implementado com o mecanismo de rotas em push e pop:
Partindo do exemplo acima, conseguimos criar um bot??o para avan??ar uma p??gina e retroceder uma p??gina, de acordo com a necessidade do usu??rio. Repare que foi necess??rio o uso do widget MaterialPageRoute para definir como a transi????o entre as telas acontecer??.
Apesar de bastante simples, esse exemplo tem um problema escondido que logo aparecer?? quando o c??digo come??ar a crescer. E este problema ?? o acoplamento das duas telas: a tela dois precisa instanciar o widget da tela tr??s. Para isso foi necess??rio importar o arquivo da tela 3 dentro da tela 2. Repare bem na seguinte linha logo no come??o do exemplo:
Outro detalhe importante, que tamb??m est?? diretamente na tela, ?? que o tipo de rota a ser utilizada foi o MaterialPageRoute. Imagine um cen??rio em que as transi????es de tela mudarem para CoupertinoPageRoute? Ou ainda que decidamos mudar todas as rotas presentes no aplicativo de push e pop para rotas nomeadas? E agora, quem poder?? nos defender? :fire:
Talvez voc?? esteja pensando agora se ?? simples de resolver. ?? s?? criar um arquivo com v??rias fun????es e cada fun????o retorna o widget da nova tela. Desta maneira conseguir??amos definir separadamente as rotas em um arquivo que pode ser importado pelos widgets que querem navegar entre telas. Por exemplo:
    """
    text_etics = """
Na filosofia, a ??tica ?? a ci??ncia que estuda sobre um conjunto de valores morais e normas comportamentais constru??da por um grupo de pessoas que definem o que ?? certo e errado. Existem diferentes c??digos de ??tica e eles variam de acordo com cada sociedade, o que ?? considerado certo para um conjunto de pessoas, pode ser errado para outras.
Se voc?? trabalha com TI, al??m dos conhecimentos t??cnicos, ?? importante agir com honestidade, respeito e dignidade diante seus colegas de trabalho, clientes e conduta ??tica da empresa, dentre outras condutas.
Voc?? sabe quais s??o as principais consequ??ncias para quem age sem ??tica no trabalho?
O que podemos considerar um comportamento ??tico no contexto da tecnologia da informa????o? ?? ??tico utilizar ou cobrar por ferramentas piratas? Acessar dados pessoais que o cliente deixou aberto no computador ?? uma atitude ??tica?
Continue lendo este artigo para saber mais sobre o assunto :)
No mercado de trabalho existem os c??digos de ??tica profissional que variam de acordo com cada profiss??o, eles s??o definidos atrav??s dos comportamentos que s??o considerados mais adequados e honestos para aquele trabalho.
As empresas tamb??m t??m os seus c??digos de ??tica e eles s??o demonstrados atrav??s da miss??o, vis??o, valores e a cultura cultivada na organiza????o. Profissionais que se preocupam e respeitam a ??tica profissional da empresa t??m maiores chances de obter sucesso no desenvolvimento de sua carreira e na constru????o de uma boa reputa????o na empresa.
Recomenda-se que profissionais da ??rea de TI precisam usufruir de suas habilidades com muita responsabilidade, j?? que a internet ?? uma rede aberta, ou seja, tenha cuidado ao manusear a informa????es, conhecendo e respeitando as leis existentes e a privacidade dos usu??rios.
A ??tica, como vimos, define o que ?? certo e errado, por??m cabe a cada profissional agir de acordo com a sua conduta ??tica na hora de trabalhar. Outros comportamentos ??ticos que um (a) profissional do segmento de TI deve ter em mente ?? da n??o utiliza????o de ferramentas ou aplicativos piratas, manipula????o de dados e informa????es e acessar recursos computacionais n??o autorizados.
    """

    def compute_freq(text):
        dic = Counter(text.lower())
        total = sum(dic.values())
        ratio = Counter(dict((letter, freq/total) for letter, freq in dic.items()))
        common = ratio.most_common(10)
        for letter, freq in common:
            print("{} => {:.2f}%".format(letter, freq*100))

    compute_freq(text_flutter)
    print()
    compute_freq(text_etics)


if __name__ == "__main__":
    test_collections()
