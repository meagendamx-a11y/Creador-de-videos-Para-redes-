# Libro de códigos v2 (regex sobre texto normalizado: minúsculas, sin acentos).
# Cada código: (etiqueta legible, definición, patrón)
import re, unicodedata

def norm(t):
    t = unicodedata.normalize('NFD', t.lower())
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')

CODES = {
 'IDENT': ('Identificación / validación',
   'El comentarista dice verse reflejado, que el video lo describe o que "no es el único".',
   r"identifiq|identific|me describ|me retrat|\bsoy yo\b(?! o)|literal(mente)? yo|literalmente (soy|me)|esa soy yo|ese soy yo|me vi reflejad|me senti reflejad|me refleje|es mi caso|mi caso exacto|exactamente (lo que|como) (me|siento|soy)|asi (me siento|soy)\b|justo (lo que|como) (me|siento|estoy)|pense que (era|solo) (el|la|yo)|crei que (era|solo) (el|la|yo)|no soy (el|la) unic|no soy (el|la) solo|me paso exactamente|todo (eso )?me pasa|me pasa (exactamente|igual|todo|lo mismo)|cumplo (con )?(todos|todas|todo)|tengo (todos|todas) (los|las)? ?(sintomas|senales|caracteristicas)|this is me|relatable|called me out|me senti (tan )?(comprendid|vist|entendid)|me hizo sentir (comprendid|vist|entendid|validad)"),
 'CONFESION': ('Confesión de malestar personal',
   'Relata sufrimiento propio actual o pasado (ansiedad, depresión, soledad, trauma, duelo, abuso).',
   r"(tengo|sufro( de)?|padezco|vivo con|me diagnosticaron|diagnosticad[oa] con|lucho con|luchando con) (una? )?(ansiedad|depresion|tdah|toc|trastorno|ataques|panico|fobia|bipolar|autismo|tept|estres|insomnio)|mi (ansiedad|depresion|trastorno|trauma)|me siento (muy |tan |demasiado )?(sol[oa]|vaci[oa]|triste|perdid[oa]|agotad[oa]|cansad[oa] de|horrible|fatal|mal\b|inutil|un fracaso|nada)|estoy (pasando por|atravesando|muy mal|en depresion|deprimid)|ganas de (morir|desaparecer|no existir|llorar)|no (puedo|aguanto) mas|ataques? de (ansiedad|panico)|me (abusaron|violaron|golpeaban|pegaban|maltrataban)|abuso (sexual|psicologico|emocional)|mi (padre|madre|papa|mama) (me )?(pegaba|golpeaba|humillaba|abandon|nunca)|perdi a mi|fallecio mi|murio mi|suicid|autolesi|me corto|cortarme|pense en quitarme|quitarme la vida|i (have|suffer from) (anxiety|depression)|i feel (so )?(alone|empty|lonely)"),
 'CRISIS': ('Señal de riesgo (ideación suicida / autolesión)',
   'Subconjunto de CONFESIÓN con mención de suicidio, autolesión o deseo de morir.',
   r"suicid|autolesi|me corto\b|cortarme|quitarme la vida|ganas de morir|quiero morir(me)?|no quiero (vivir|existir)|desaparecer para siempre|kill myself|want to die"),
 'AYUDA': ('Pedido de ayuda / consejo',
   'Pregunta qué hacer con un problema propio o pide ayuda directa.',
   r"(que|q) (hago|puedo hacer|debo hacer|me recomienda[ns]?|me aconseja[ns]?)\s*(\?|por favor|porfa|doctor|dra|dr)|(que|q) me recomienda[ns]?|necesito (ayuda|un consejo|consejo|hablar con alguien)|ayudenme|ayudame\b|alguien (me )?(puede|podria) (ayudar|aconsejar|orientar)|algun consejo|como (salgo|supero|dejo de|hago para|puedo dejar|controlo|le hago)[^?]{0,80}\?|me pueden (ayudar|aconsejar|orientar)|help me|any advice"),
 'PIDE_TEMA': ('Petición de tema / próximo video',
   'Solicita explícitamente un video, tema, continuación o profundización.',
   r"\b(haz|hagan|haga|harias|harian|podrias hacer|podria hacer|podrian hacer|puedes hacer|pueden hacer|deberias hacer|deberian hacer|ojala hagas|ojala hagan)\b[^.!?]{0,25}\b(video|tema|analisis|parte|capitulo|episodio|uno)\b|\b(podrias|podria|podrian|puedes|pueden|deberias|ojala|me gustaria que|me encantaria que|quisiera que)\b[^.!?]{0,15}\b(hablar|hablaras|hablaran|hables|explicar|explicaras|abordar|tocar|analizar|analizaras)\b|\b(hablen|hables|habla|analiza|analicen)\b (de|sobre|acerca) |(un|otro|algun) video (sobre|acerca|del tema|de como)|parte 2|segunda parte|parte dos|(me gustaria|me encantaria|quisiera|espero) (ver )?(un|otro) video|tema (para|de) (un|el proximo|tu proximo) video|(por favor|porfa)[^.!?]{0,20}video (de|sobre)|please (make|do) a video|make a video|part 2|mas videos (de|sobre|como este)"),
 'GRATITUD': ('Gratitud / utilidad percibida',
   'Agradece o afirma que el video le sirvió, le ayudó o le dio claridad.',
   r"gracias|me (ayudo|ayuda|sirvio|sirve) (mucho|bastante|un monton)?|muy util|me abriste los ojos|me abrio los ojos|necesitaba (escuchar|oir|ver) (esto|eso)|llego en el momento|justo lo que necesitaba|thank"),
 'CLARIDAD': ('Elogio a la claridad / forma de explicar',
   'Elogia que se explica claro, sencillo, ameno o con ejemplos.',
   r"explica(s|n|ste|cion)? (muy |tan |super |de manera )?(bien|clar|sencill|facil|simple|ameno|excelente)|(muy|tan|super) (clar[oa]|did[aá]ctic|ameno|entendible|sencill)|(facil|sencillo) de entender|lo explicas|como lo explicas|didactic|bien explicado|clear explanation|well explained"),
 'VOZ': ('Mención de la voz / narración',
   'Cualquier mención a la voz, el narrador, la locución o la forma de hablar.',
   r"\b(tu|su|la|esa|que|una) voz\b(?! (se|me) (quiebra|tiembla))|narrador|narradora|narracion|locucion|locutor(?!.*radio)|tono de voz|tu forma de hablar|\bvoice\b|narrat"),
 'VOZ_POS': ('Elogio a la voz',
   'Mención positiva de la voz (calma, cálida, agradable, humana).',
   r"(voz|narracion|locucion|forma de hablar)[^.!?]{0,30}(linda|hermosa|bonita|preciosa|relajante|tranquil|calma|calid|dulce|agradable|suave|encanta|bella|genial|perfecta|paz|reconfort|me gusta)|(encanta|amo|adoro|me gusta|relaja|tranquiliza|calma)[^.!?]{0,25}(tu |su |la )?(voz|narracion)|(soothing|calming|lovely|beautiful|love (the|your)) voice|voice is (so )?(soothing|calming|beautiful|lovely)"),
 'VISUAL': ('Mención a animación / dibujo / personaje / estilo visual',
   'Menciona animación, ilustración, personaje, colores, edición o estética.',
   r"animaci|animad[oa]s? (es|son|esta)|dibujo|dibujos|dibujit|dibujad|ilustrac|monit[oa]s?\b|munequit|caricatur|estilo (visual|de dibujo)|la edicion|edicion (del|es|esta|me)|los visuales|art style|animation|drawing|illustrat"),
 'MINIATURA': ('Mención a la miniatura (thumbnail)',
   'Menciona la miniatura del video (a menudo como broma o gancho).',
   r"miniatura|thumbnail"),
 'MUSICA': ('Mención a la música / sonido',
   'Menciona la música o el sonido de fondo.',
   r"musica de fondo|la musica (del|de este|de tu|de los) (video|canal)|(la|esa) musica (es|esta|me|queda|le)|cancion (del|de este) video|banda sonora|soundtrack|background music"),
 'CRIT_IA': ('Crítica / sospecha de IA',
   'Señala o sospecha que el contenido, la voz o las imágenes están hechos con IA o suenan genéricos/robóticos.',
   r"chat ?gpt|\bgpt\b|(hech[oa]|hace[ns]?|creado|generad[oa]|usas|usan|usar|animaciones?|imagenes|voz|guion|texto|video|contenido|basura|dibujos?|narracion)\b[^.!?]{0,15}\b(con |por |de |en )?(la )?(\bia\b|inteligencia artificial|\bai\b)|(\bia\b|inteligencia artificial)[^.!?]{0,20}(guion|voz|animaci|imagen|dibuj|video|basura|contenido)|voz (robotica|de robot|artificial|sintetica|generada)|robotic voice|ai generated|ai slop"),
 'CRIT_EXACT': ('Crítica de exactitud / rigor',
   'Cuestiona la veracidad, falta de fuentes, generalizaciones o errores conceptuales.',
   r"\bfuente(s)?\b|\bevidencia\b|estudios? (cientific|que lo|que demuest|serios)|pseudo|desinform|\bfalso\b|incorrect|(eso|esto) no es (asi|cierto|correcto|verdad)|no es (cierto|correcto) (que|lo que)|te equivocas|se equivoca|esta equivocad|error (en el video|grave|conceptual)|generaliza[rn]?\b|generalizacion|simplista|demasiado (simple|general|generico)|confund(e|es|en|iendo)|mezcla[ns]? conceptos|no tiene (base|sustento) (cientific|teoric)|cientificamente|misinformation|not true|pseudoscience"),
 'CRIT_PATOLOG': ('Crítica a la patologización / etiquetas',
   'Rechaza convertir rasgos normales en trastornos, autodiagnóstico, romantizar o victimizar.',
   r"patologiz|no todo es (un )?(trastorno|trauma|ansiedad|depresion|toxico|narcis)|ahora todo (es|el mundo)|ahora resulta que|todo es (trauma|toxico|narcis)|todo el mundo es (narcis|toxic|bipolar)|todos (somos|son) (narcis|toxic|bipolar)|autodiagnost|auto ?diagnost|diagnosticarse (solo|por youtube|con un video)|romantiz|se victimiza|victimizarse|victimizacion|no es (una )?(enfermedad|trastorno)|es solo ser humano|eso es ser humano|overdiagnos|pathologi|self.?diagnos|etiquetar"),
 'HOROSCOPO': ('Efecto horóscopo / Barnum',
   'Señala que las descripciones aplican a cualquiera, como un horóscopo.',
   r"horoscopo|barnum|forer|signo zodiacal|aplica (para|a) (todos|cualquiera|todo el mundo)|le pasa a todo el mundo|cualquiera se (siente|identifica)|todo el mundo (es|hace|siente) (asi|eso)|eso lo hace todo el mundo|eso es (ser )?(normal|humano)|cambien .{1,20} por cualquier|descripciones genericas|everyone (does|feels) (this|that)|horoscope"),
 'TERAPIA': ('Mención a terapia / psicólogo / psiquiatra',
   'Cualquier mención a terapia, psicólogo, terapeuta, psiquiatra, consulta.',
   r"(?<!quimio)terapia(?! (es|para mi) (escuchar|limpiar|caminar|la musica))|terapeuta|psicolog[oa]s?\b|psicologa|psiquiatra|psicoterap|consulta (psicolog|con un)|ir al psic|tratamiento psicolog|therap|psychologist|psychiatrist|counsel"),
 'TER_POS': ('Terapia: experiencia/actitud positiva',
   'Dice que la terapia le ayuda, va a terapia, la recomienda.',
   r"(la |mi )?terapia (me )?(ayudo|ayuda|salvo|cambio|sirve|sirvio|funciona)|(voy|iba|fui|empece|comence|estoy (yendo|en)) (a |en )?(terapia|psicolog|con (una|un|mi) (psicolog|terapeuta))|gracias a (la terapia|mi (psicolog|terapeuta|psiquiatra))|mi (psicolog[oa]|terapeuta|psiquiatra) (me )?(dijo|ayudo|explico|recomend|ensen)|recomiendo (ir a |la )?terapia|vayan a terapia|ve a terapia|busca(r)? (ayuda )?(profesional|un psicolog|una psicolog|terapia)|ayuda profesional|therapy (helped|changed|saved)"),
 'TER_NEG': ('Terapia: experiencia/actitud negativa',
   'Mala experiencia, desconfianza o la terapia "no sirvió".',
   r"terapia (no )?(no me )?(sirve|sirvio|ayudo|funciono) (de nada|para nada)|(terapia|psicolog[oa]s?|terapeuta) no (me )?(sirv|ayud|funcion|entend|escuch)|mal(a|o)s? (psicolog|terapeut|experiencia)|psicolog[oa]s? (me )?(juzg|minimiz|ignor)|perdi (mi |el )?(dinero|tiempo) (en|con)|no creo en (la terapia|los psicolog)|los psicologos (solo|no sirven)|cambie de (psicolog|terapeut)|ya fui a (varios|muchos|varias|muchas)"),
 'TER_COSTO': ('Terapia: costo / acceso',
   'Menciona precio, no poder pagar, falta de acceso, gratuidad, sistema público.',
   r"(terapia|psicolog|terapeuta|psiquiatra|consulta)[^.!?]{0,60}(cara|caro|caros|caras|costos|costosa|precio|dinero|pagar|plata|gratis|gratuit|economic|lujo|privilegio|seguro|imss|issste|publica|no tengo para)|(no (tengo|me alcanza)|no puedo pagar|sin dinero|cobran|pagar)[^.!?]{0,60}(terapia|psicolog|terapeuta|psiquiatra|consulta)|terapia gratis|psicologo gratis|consulta gratis|can'?t afford|expensive"),
 'TER_MIEDO': ('Terapia: miedo / estigma / vergüenza',
   'Miedo, vergüenza, estigma ("es para locos"), no saber cómo empezar o resistencia familiar.',
   r"(miedo|verguenza|pena|me da cosa|no me atrevo|nunca me he atrevido|no se como empezar|temor)[^.!?]{0,50}(terapia|psicolog|terapeuta|psiquiatra|ayuda profesional)|(terapia|psicolog|psiquiatra)[^.!?]{0,50}(miedo|verguenza|pena|locos|loco|loca|estigma|no se como empezar|juzg)|(para locos|no estoy loc[oa])|mis padres no (me dejan|creen)[^.!?]{0,40}(terapia|psicolog)|stigma"),
 'VIDEO_COMO_TERAPIA': ('El video como sustituto de terapia',
   'Dice que el video es "terapia gratis", mejor que su psicólogo o que le ahorró una consulta.',
   r"terapia gratis|sesion (de terapia )?gratis|consulta gratis|mejor que (mi |un |una |el |la |cualquier )?(psicolog|terapeut|terapia)|me ahorr(e|aste)[^.!?]{0,30}(terapia|psicolog|sesion)|(es|fue|como|parece) (una )?(sesion de )?terapia|ni mi (psicolog|terapeuta)|mas que (mi |un |una )?(psicolog|terapeut|terapia)|free therapy|better than (my )?therap"),
 'HUMOR': ('Humor / broma',
   'Risas, bromas, memes, ironía explícita.',
   r"\bja(ja)+|\bje(je)+|\bjsj|\bxd+\b|\blol\b|😂|🤣|😆|lmao|\bjajs|\bkk+\b"),
 'COMUNIDAD': ('Comunidad / apoyo entre comentaristas',
   'Se dirige a otros comentaristas, envía ánimo, "no estamos solos", "¿alguien más?".',
   r"no estamos sol|no estas sol[oa]|no estan sol|a (todos )?(los|las) que (estan|lean|leen|pasan|sienten)|quien (mas|lea|esta)|alguien mas|si alguien (lee|esta)|les mando|te mando un abrazo|un abrazo (a todos|para todos|enorme)|abrazo (para|a) (todos|quien)|animo a todos|fuerza a todos|mucha fuerza|aqui estamos|somos (muchos|varios)|leyendo los comentarios|los comentarios (son|me)|en los comentarios|comunidad|anyone else|you are not alone|we are not alone"),
 'FE': ('Religión / fe',
   'Menciona Dios, Jesús, oración, Biblia.',
   r"\bdios\b|jesus|cristo|biblia|oracion|\borar\b|\bamen\b|senor jesus|espiritu santo|\bgod\b"),
 'FAMILIA': ('Infancia / padres / crianza',
   'Menciona infancia, padres, crianza, hijos.',
   r"infancia|ninez|de nin[oa]|cuando era (nin|pequen|chic)|mis padres|mi (padre|madre|papa|mama)\b|crianza|mis hijos|mi hij[oa]|childhood|my parents"),
 'PAREJA': ('Pareja / relaciones amorosas',
   'Menciona pareja, ex, novio/a, esposo/a, ruptura, amor romántico.',
   r"pareja|mi ex\b|\bex (pareja|novi)|novi[oa]|espos[oa]|marido|ruptura|terminamos|me dejo\b|relacion (amorosa|toxica|de pareja)|enamor|boyfriend|girlfriend|my ex\b"),
 'CRIT_FORMA': ('Crítica de forma (duración, clickbait, relleno, anuncios)',
   'Se queja de duración, relleno, título engañoso, repetición o publicidad.',
   r"clickbait|click ?bait|titulo enganoso|relleno|muy largo|demasiado largo|muy corto|ve al grano|al grano|repetitiv|siempre (lo mismo|dices lo mismo)|mucha publicidad|demasiados anuncios|anuncio|vende humo|vendehumo|solo (quiere|quieren) vender|curso|too long"),
 'ELOGIO_GEN': ('Elogio general al video / canal',
   'Elogio genérico ("excelente", "me encanta tu canal", "gran video").',
   r"excelente|me encanta (tu|este|el) (canal|contenido|video)|me encantan tus videos|gran video|buenisim|muy buen(o)? video|maravillos|increible video|que buen video|amo (tu|este) canal|great video|love this channel"),
 'HUMANO': ('Valoración de lo humano / auténtico / experiencia del profesional',
   'Valora calidez, empatía, autenticidad, que "se nota que sabe" o habla desde la experiencia.',
   r"se nota que (sabes|eres|te importa|lo has vivido|lo vivi)|autentic|(tu|su|con|mucha|tanta) empatia|calidez|calid[oa]|cercan[oa]|humild|habl(as|a) desde (la|tu) experiencia|con (tanto )?(amor|carino)|transmites (paz|calma|confianza)|me transmite|eres (un ser |una persona )?(hermos|maravillos|lind)|genuin"),
}
COMPILED = {k: re.compile(v[2]) for k, v in CODES.items()}

def code(text):
    t = norm(text)
    return [k for k, p in COMPILED.items() if p.search(t)]

ES = set('que de la el en y los se del las un por con no una su para es al lo como mas pero sus le ya o este si porque esta entre cuando muy sin sobre tambien me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mi antes algunos yo otro otras otra el tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros mis tu te ti tus soy siento video gracias'.split())
EN = set('the and to of a in is you that it for this i my are with on be your have me but not was they so do just what like can about when if all video people feel'.split())
PT = set('voce nao muito obrigado obrigada isso eu tambem sou ate meu minha'.split())

def lang(text):
    w = re.findall(r"[a-záéíóúñü']+", text.lower())
    if not w: return 'otro'
    wn = [norm(x) for x in w]
    es = sum(x in ES for x in wn); en = sum(x in EN for x in wn); pt = sum(x in PT for x in wn)
    if pt > es and pt > en: return 'pt'
    if es == 0 and en == 0: return 'otro'
    return 'es' if es >= en else 'en'
