# scikit-image-examples
Aprendizado e teste com a lib [scikit-image python](https://scikit-image.org).

### 1 - Colorindo imagens em escala de cinza
Pode ser útil tingir artificialmente uma imagem com alguma cor, seja para destacar regiões específicas de uma imagem ou talvez apenas para animar uma imagem em tons de cinza. Este exemplo demonstra o tingimento da imagem dimensionando os valores RGB e ajustando as cores no espaço de cores HSV.

  - Em 2D, as imagens coloridas são frequentemente representadas em RGB - 3 camadas de matrizes 2D, onde as 3 camadas representam os canais (R) ed, (G) reen e (B) lue da imagem. A   maneira mais simples de obter uma imagem colorida é definir cada canal RGB para a imagem em tons de cinza dimensionada por um multiplicador diferente para cada canal. Por       exemplo, multiplicar os canais verde e azul por 0 deixa apenas o canal vermelho e produz uma imagem vermelha brilhante. Da mesma forma, zerar o canal azul deixa apenas os      canais   vermelho e verde, que se combinam para formar o amarelo. 

### 2 - Modelo de Contorno Ativo
O modelo de contorno ativo é um método para ajustar splines abertas ou fechadas a linhas ou arestas em uma imagem 1. Ele funciona minimizando uma energia que é em parte definida pela imagem e parte pela forma da spline: comprimento e suavidade. A minimização é feita implicitamente na energia da forma e explicitamente na energia da imagem.

Nos dois exemplos a seguir, o modelo de contorno ativo é usado (1) para segmentar o rosto de uma pessoa do resto de uma imagem ajustando uma curva fechada às bordas do rosto e (2) para encontrar a curva mais escura entre dois Pontos, obedecendo a considerações de suavidade. Normalmente, é uma boa ideia suavizar um pouco as imagens antes de analisá-las, como feito nos exemplos a seguir.

Inicializamos um círculo ao redor do rosto do astronauta e usamos a condição de limite padrão boundary_condition = 'periódica' para ajustar uma curva fechada. Os parâmetros padrão w_line = 0, w_edge = 1 farão a pesquisa da curva em direção às arestas, como os limites da face.


### 3- Usando transformações polares e log-polares para registro
A correlação de fase (registration.phase_cross_correlation) é um método eficiente para determinar o deslocamento de translação entre pares de imagens semelhantes. No entanto, essa abordagem depende de uma quase ausência de diferenças de rotação / escala entre as imagens, que são típicas em exemplos do mundo real.

Para recuperar as diferenças de rotação e escala entre duas imagens, podemos tirar proveito de duas propriedades geométricas da transformada log-polar e da invariância de translação do domínio da frequência. Primeiro, a rotação no espaço cartesiano torna-se translação ao longo do eixo de coordenadas angulares (θθ) do espaço log-polar. Em segundo lugar, a escala no espaço cartesiano torna-se translação ao longo da coordenada radial (ρ = lnx2 + y2 −−−−−−− √ρ = ln⁡x2 + y2) do espaço log-polar. Finalmente, as diferenças na tradução no domínio espacial não impactam o espectro de magnitude no domínio da frequência.

Nesta série de exemplos, construímos esses conceitos para mostrar como a transformada log-polar transform.warp_polar pode ser usada em conjunto com a correlação de fase para recuperar as diferenças de rotação e escala entre duas imagens que também têm um deslocamento de translação.

- Recupere a diferença de rotação com uma transformação polar
  - Neste exemplo, consideramos o caso simples de duas imagens que diferem apenas no que diz respeito à rotação em torno de um ponto central comum. Ao remapear essas imagens no espaço polar, a diferença de rotação se torna uma diferença de translação simples que pode ser recuperada por correlação de fase.

### 4 - Deconvolução de imagem
  Neste exemplo, deconvolvemos uma versão barulhenta de uma imagem usando Wiener e algoritmos de Wiener não supervisionados. Esses algoritmos são baseados em modelos lineares que não podem restaurar bordas nítidas tanto quanto métodos não lineares (como restauração de TV), mas são muito mais rápidos.
  ### 4.1 - Filtro Wiener
  - O filtro inverso é baseado no PSF (Point Spread Function), na regularização anterior (penalização de alta frequência) e na compensação entre os dados e a adequação anterior. O   parâmetro de regularização deve ser ajustado manualmente. 
  -   ### 4.2 - Wiener não supervisionado
  - Este algoritmo possui parâmetros de regularização autoajustados com base no aprendizado de dados. Isso não é comum e é baseado na seguinte publicação 1. O algoritmo é baseado em   um amostrador de Gibbs iterativo que extrai amostras alternativas da lei condicional posterior da imagem, a potência do ruído e a potência da frequência da imagem.

### 5 - Segmentação de Chan-Vese
  - O algoritmo de segmentação Chan-Vese é projetado para segmentar objetos sem limites claramente definidos. Este algoritmo é baseado em conjuntos de níveis que são evoluídos iterativamente para minimizar uma energia, que é definida por valores ponderados que correspondem à soma das diferenças de intensidade do valor médio fora da região segmentada, a soma das diferenças do valor médio dentro da região segmentada , e um termo que depende do comprimento do limite da região segmentada.

  - Este algoritmo foi proposto pela primeira vez por Tony Chan e Luminita Vese, em uma publicação intitulada “An Active Contour Model Without Edges” 1. Ver também 2, 3.

  - Esta implementação do algoritmo é um tanto simplificada no sentido de que o fator de área ‘nu’ descrito no artigo original não é implementado e só é adequado para imagens em tons de cinza.

  - Os valores típicos para lambda1 e lambda2 são 1. Se o 'fundo' for muito diferente do objeto segmentado em termos de distribuição (por exemplo, uma imagem preta uniforme com figuras de intensidade variável), então esses valores devem ser diferentes uns dos outros.

  - Os valores típicos para mu estão entre 0 e 1, embora valores mais altos possam ser usados ​​ao lidar com formas com contornos muito mal definidos.

  - O algoritmo também retorna uma lista de valores que corresponde à energia em cada iteração. Isso pode ser usado para ajustar os vários parâmetros descritos acima.
