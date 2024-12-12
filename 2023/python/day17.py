from collections import defaultdict
import heapq

def djikstra(sources, neighborsFunc):
  inf = 10**20
  
  vis = set()
  dist = {}
  Q = []
  for source in sources:
    dist[source] = 0
    Q += [(0, source)]
  while Q:
    _, u = heapq.heappop(Q)
    if u in vis: continue
    vis.add(u)
    for nei, cost in neighborsFunc(u):
      tmp = dist[u] + cost
      if nei not in dist or tmp < dist[nei]:
        dist[nei] = tmp
        heapq.heappush(Q, (dist[nei], nei))
  return dist

def solve1(s):
  a = s.strip().split("\n")
  a = [ list(map(int, row)) for row in a]
  n, m = len(a), len(a[0])
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  def inside(i, j): return 0 <= i < n and 0 <= j < m

  def neighbors(state): # returns list of (neighbor, cost) pairs
    i, j, dir, ct = state
    ndir = (-dir[0], -dir[1])
    for d in dirs:
      ni, nj = i + d[0], j + d[1]
      if d == ndir: continue
      elif d == dir:
        if ct < 3 and inside(ni, nj):
          yield (ni, nj, d, ct + 1), a[ni][nj]
      else:
        if inside(ni, nj): yield(ni, nj, d, 1), a[ni][nj]

  dist = djikstra([(0, 0, (0, 1), 0)], neighbors)
  mincost = 10**100
  for (i, j, dir, ct), cost in dist.items():
    if i == n - 1 and j == m - 1: mincost = min(mincost, cost)
  print("Part 1:", mincost)
def solve2(s):
  a = s.strip().split("\n")
  a = [list(map(int, row)) for row in a]
  n, m = len(a), len(a[0])
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  def inside(i, j): return 0 <= i < n and 0 <= j < m

  def neighbors(state): # returns list of (neighbor, cost) pairs
    i, j, dir, ct = state
    ndir = (-dir[0], -dir[1])
    for d in dirs:
      ni, nj = i + d[0], j + d[1]
      if d == ndir: continue
      elif d == dir: 
        if ct < 10 and inside(ni, nj): yield (ni, nj, d, ct + 1), a[ni][nj]
      else: 
        if ct >= 4 and inside(ni, nj): yield(ni, nj, d, 1), a[ni][nj]

  mincost = 10**100
  for (i, j, dir, ct), cost in djikstra([(0, 0, (0, 1), 0), (0, 0, (1, 0), 0)], neighbors).items():
    if i == n - 1 and j == m - 1 and ct >= 4: mincost = min(mincost, cost)
  print("Part 2:", mincost)
def solve(s):
  solve1(s)
  solve2(s)

solve("""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""")

solve2("""
111111111111
999999999991
999999999991
999999999991
999999999991
""")

solve("""
222122222223113222232332334342314311221224331555341315113141344525243452541321241454225245341444551311241314442331214243423113133331332322222
121213232332313311221314142113232232211333525123352551344351122352133553145232234115321453351214241353332423344411413144431213323223222213222
212332133133331231313241313311443144333445435431153143452442121321314115423151143442453314142345241441221232333242241121223112323311213131332
121223111221213131223241214123111413132533151553154141153144114123154242235422215312244445531223323412431442313144214122141223121123312121111
231333223211332134113131113324443243254514214123215545551241532433523555331531442545231335525343444132325122323311344424222133233311112123131
313232323113311133342343321311414244545354224141541525331541444512431115122145521333544553211141332454355411142443412142344431123313232311311
111132121113233332144312312413142554254255234145214141352424531233354665342515523342241244545542522415414534422143431124113131142231111321211
233122122221133243231343114242354123333242214253511215113435343565333265332243225462355444243354311215222412243513342413324442223112232223323
322233132132132232322142242211541132344354411332111152265363444436632265622532236656255335234443355513324153155424413141233123431122321223212
222312223212344221334433341421154455141423545355241156636263665566345645626562545644236352232225155152241542523321414141223422442213332333322
311332311244343123234314321422122412332453222214152646322263464324424562646354663443634666225544414325232523545124143131314112444242133133322
211212133234423121441324213241113552345212141553465464426632325643645532226526523665645346552454544342142532425323351323234413111331133221323
211121322123412111341224512435241214112445234625336246446534256255564456236662263542355465556233555155542122452123451151331232443432332332322
212323321123144434322131143235222511314352344256426532552666446245242645346544545453234224466333436333144314253333244551242114121323312123322
332321121211434321111422533243421525525562642625333422524534336244236324426423233254424245366552324542451115352542354331231334223443311223232
321214442412113322113243524141441525544456535645466454565544463422322456433334525336252245462452342443333252153114122532145334422411223412333
112113143413411331412332141422142454233566333533652666256266636654564246452662254546266443424246252225635435314454425111152521112333431231213
333322423214231422123311211553443122632453556456446654263563344536444367536333464634542666345334324554225222412331251313222322321111223133121
322143421422323433325155133112123164365424654466665654334643774353355466677376635372256653533432636455262242443132222425435543222212113333131
321412322322243223435155422135215222324425333443252355246356435563637767473444757444453465362262545633433363564154453453254242414421144113234
222342441223324142351453335312535522334434334355335523764676637333633566535335755747543467632466634425445453225655231512325134453314242124433
241414441332414151254415425122435552545453653446426736347673544537755574467334577367635537664256352263432363664333442451234532553434313114214
142141343234435232142551342144323653426264225634476537335674674643365473346643456474357453565473354226442526243524434352122212412424441322122
212241432243153552225424554142335632353662266453745456453674453446333533764466474737464533433566522366663532666422324521441535141331112423123
324223243221234232152324142534324365535662444647766365534447535655464636477543643777756634774435757565334632222324342322553112343541232344422
424443444441525512521154452234632233555234633547765576735454575574367633473757565644734557774665454643352556454444434351153223142324244312124
132122122441234235122444346253256655663627555455543743473633335537735776753755336735465354677473736477344252644532536345122112232444132211324
332334312424452215552443653442635456235675543373743777677746556664673576547753573443643443477574444465462233546526365222525314431123513131114
442112443514443215411242462555433666225376366367354353667444675663545555554855776635564757774576453763354262533346534532552434425324344142442
131232322241341442542135234334324445336456774473737655636743575874476758748447666747535566373475547357346552262254453554421224552253241133111
144321212311113331413645553553424442474454744657776743635547474856867566747755654566463436454435655775577346646443464643542552335221324322223
312341415141453514325564262423524646733777335774467336466768665767677655884776886764548756557765666667367366666224255652545215514121535131424
443213524143453331542365442562453467744576444534536678654776664685547475886568688848644646457355637467353657426465222655336554252421153351442
234212223523522221355242256445625356444657443336337865475848687556648646576846554875868885745364576746666363636245545535642421122454234134324
413125535222533352342466423562455377367634677645367648547557766676484848558446865568766854666554437577375475466346353532225562352344133514122
233145325135113143555336552234436773376355434734448676558654886557465877655684446786567688684744356463757546646354465346522445455352533133111
122425151533511216326554546445746655755655645647666474664854454566556754788685646854484846687885864755756743333742266322363322215455434412342
341455233415423133433455553543765365474733465856885688685754866587848776848675665666868754668878586366735543474364546665654223211413411214544
244143512523342254345534253575674663676366778745655868468564847866848585455758567867684668674554754743477373454743464233526543345115442223151
243452251215222663536333224465547736335653545776874575856757575766878896789585874855855487787774685453356337746774345636465356623451211222452
145121532345433333524626536455734344345737447768478867774787756689997599697665977786874688878867754776336447364667353653256554632521512533211
214223323544253254422346444776674764376744568845685885557476598696989765658568576655545856475785555776773467643755463346422324446125214155554
132143412451365634464656535776344744454544885865654865848788569788779789595599997865556456875646745545783566437375637232255225466633414544313
343434124322236344445262274377334334578866567858447746879769667559878698559988669795555586574548485485844465434773467723266436442233413425544
432241315524232353343363467777754544346846664655685867989798795679979695899785685887588966688786764444564763377743764764322662565522411312215
341141235242235522564324374735356366585754464775888668565595785588886595888698597859777988945846488584557446466576575672656646346343541152135
221314132216252656525255576673454337558757658566745675795858755998587875858959997955689998897758864648845843373737645563324622442252344343212
411154543444426555623464757336476646486847585758468695678956956767667756595757977699879758589688484858446587345756754674642426464224235242345
522153422315454564525634363536535768778787878476956996659857557795585797959975798997677869888768765456464564747533447336353665453322313423245
213231553262463536342543375335764588588755547887967669797777956958996587558596699797578858965898784586775844455565356734452323434546655123341
145224214446646653334574345633747657568768578848956765688788985688667796766889658597776777958997575574564875443754446773544354566345221552432
451214213125553465554564754536764648575758545777769595656768759766788896669677665559975756556789877667476666464555777374443522233654631531352
335343131424362563666543533537567855575585887699596567577668698679989969778689786657986577689687968686645454687653536566362323352644552434432
213542552434653252457576663657448556486448645999678689569656988676898798689689699669668675589957896877846468668736344776563446633342453244114
333415452224546446633777446747658476874576457779996799677796678888678998969878786987688968875896865885756586646755745755345223436636261414533
135232325665654555266656653347548847847458489788596565955879678776999776887966987868799999966696877875774747568456544544646625665255452425535
342451223564226523554344677765665866784557485989978787679998698796897779696768889679889675768988588556884674855575473655355445466333344133514
314155145424354452475465445373766557656675578666789779897977997876787966988767999766668957999768875696755756478453743557335542366545342242421
524354322645522626534654774676767485865665768577969956766968779666767768979787786767799997875567775578654548468665373764653556634534233332543
222431455562524443255757475563875756475778658659978867886978669786698788886667797688767799668775575769465754865776563347554735556235523213532
422143166342563266756377365476648687774548786768868978768768678887667778786888698678668989966785677659775455485766556456563336465625522612452
424332122444465344754767363578475676554458795698778667679876786887679887988786766777677666979959895755476856667758536346355643242562625222221
154411143236334323356756644767467678687879958887965897999899679887889978777788797866979787786868987596888886775774353757733646232626242554415
125542462244242542745636467777585584544795897656655798989899878897887897798997798977698679679968789556655847866754334644765342443442264431455
125141534445565366376653546567476866864887579556696896696777898979778999979779876978678866778556589658875747856667366537335534254555354225323
344234153226435452734356463566478784788457898589567699787766687997977799997899889666666869696695996988966456454446665354436533422366425623235
533115533542422655746746746375558656567668657695787796876776677997799787987798789789696698867877658667995748845685734655433762243536466644124
255131466663333544547674375366446476486586887585987897997999897989798878798898998966896976767668587589698856655758774334456633626354553622144
233151444364454356435755673588675785588756577599958877687998998989978989979978997877876989779985855665794678546558467645354764244253233353514
353153364332534336475474734565666585556687888888967988999868889778788779997877787999869967767666867876767745776675877776336434644225643235245
321441346534654544557465637547688886546888656789868688766788987788989788888989899776667698869959576685998574446856577663365333244242534424541
313522623362344634367656356687566487588669895965577669687978788887877898789787887967667976696578867557874456547546455676654563665233322253452
553523463322332644767765654765775868564756656588758887697686778998988989898788987886787778778778895759785667766756767376347457243435546325311
113321335452642464744645454385567557685865568987677678776887999879789979989779988779699678779765686799976446654844435566663746535553246633252
125235163552334346667734777676548785644898587555678897676898788878889898898899779778989767998699855765655578565566677475435643423553556344111
122211355542232444546637663585676786667758558866657786696866979977789989997798899977878678686585965987676687557764856643465477262625245523515
341311322562552444465534553644746646476596598856589679698669879889979899999798799886696987866669689876987765648644836433533563234265655354134
131254356642562425376555537664457787887886855578959996998996899879898887777799889797789969779695655766844445676446374475444665224535365412151
421552125432363562565446645566874758558878866679797789766679889878998778777779896778989997666955896798746876466787454656655473356235422354235
521515446632656352573753555668878875658566776789566766868869787899979879789899797986789789998895867777658685758688747745773343644555234434225
545352334433552455434556374368586458565566865596656668786677899879899797779998897788887879689889995588678456584655533535355765462422653255125
441544164242623255657545663747444858486488975596686598676687777696678799997897867986787796866585857558565545857444366653354374555534466624444
221151442446265243753337537643744468458846997667585696696786666689879779898689866798788966695969857678687677875787375665337455555653642654232
522143334253525665543576333763458765754575578969579558867977967898799689886899797879777978789955599679456576664563454453755665556565655542222
113445144363524666676467336755764885557456797685998577699977988676797769866899796769969769975579575896585846877664746637663552652454546553441
312244456255662663274665466444566567576778758787689895978699767889777896677966997679768999567678555658744587558663343677664353362355534232133
141145535352323633234445357566357675566657557655575789867976789887967896779876689876989757588768855647748447667854536735653452336642254354112
121114254365532346353555634757448466844876795896877876656869768897778977677967768867887967786896956665868448578875555575347533643255263443245
122133331532224444366663456434338875474758678985667556755667678866798896897878997998686677597968679857475686674567665336544366466452663254311
224224153424654624535556743576537466485788848688566556699869779689769869689699798779667958755676578676857877866535555453557645656566664415342
224412522433645463365363447746753885767686558955897995988655677897989889697977978899798785558696685645876876765756675435356433233562561234342
445552121442223423565436654745767488655656887695698769885955979996778669687678796897687757758757556478545754573477374545354432243246443522243
421354115152634625453434674745675646677568555485996755686879968867869979996985986965655967666998767455856565865453474467764342533344641441153
553241254264552246244456445647577678448566778566585699966996888665768699989779595665855795576675656474655654875754767566543323334645512354325
513343333243366452565635467733746675445484688555956566676765767788775565598756797887997579989995454645867445763664355345753536433546143123121
125131551223345346542365577337735556764875667754446865555966676679698855599686985875996676799855858748555674635667545667225664335566155212211
511124412535445664232337633455575477464687677675446668679789876996569899779867967656657757864774867855845567637774636473554462625324433455255
333314212551634636626534545435636337557455465866667695855796585899756795665695786759897966874665786658866446444455567535263654242354351454515
333352144512326562436642635454757737676867646488444679898969996657988869567668567969896858485455776455545436733657756334335246623544322415324
351433553425525665252454443644643355457768467488554586658996679555657985795566997786585858654456586688655556643344773622544535545241211233123
244551411422446422662235264545777776655864464678646548558969799559955877976595877867696686784555666746454473773646763634354566464411325233545
134442342131436254553545263735357336477388646646688586845485895987685788657656656986545688768585556756464345567765735562365365236244543232344
413424243312345433424642525745636647737544884575545546487785868679765885886987968886567578686755875667577773346776636326256664555142222441515
224542222225412325624622445567753666566757567784677478478858844466556695696575757668674577846566687644653556764564563422225356665221125425212
224541123452243436552265622345354447475565774755888654855458465744878664675457848458774748654568654565466765754454426233634366434513332423532
111111131122533246224536266354375433566774453858587587587776555677755565757778787868885575785556544467476665476573326645653334455151335142123
314335325352251424453524265566455555434747453374864565647686884545454746654665656544555885876555453356665347647556364344634626151422114443123
132315545432243122234425444525443357745546543555654885447886874457578677867865545647547544757688735336355345676532422436626645321214124134212
443323231424534343466635666222526457464735666667668856674447785858874486477766486647686575855765546456545434677434545252435341445255332154241
112132355244213155233442235466434765766475536356756684465575864445764858786785447447456546876757643366356365533325522463622314154332523412222
142114432255353453443333242364454445455667565746775338455775466464446566858545476774748684744466355663347557725225254556442215332133253233113
324232222353554311553264345636223425446373753365633364466564568868468884445465874857688447555536455333533655225643634443235332351244433213223
321433314313354144232435524663626536674567763664547375777767588455666548645778654885544464643677477434474675433526362636332114334554441324114
444321112222334134433263345652652235534675767667776437555467577585866545875486664634566453575434737677576733446345256355453543353114412143334
334213333552335224223433264463565555325776453574746463574563756633564685485754464533647434737337665734565563342354236662235252132554241324333
144242213332514333152434432345554565264335637367775737335764737743676544744566376673745757745533364645453343235662625363513324113323243414331
421244234231131113244435543362364532632556547634376347443334636346766373467547446657376566637376376645435656232353325235532515111344441122314
432221443343421433442334254443544645225462444464345667466447446353676465637574566575435537655465434753443533653564366253512344224523214124314
442411214142453325332355511645664334543632657346365355435344476755567436477367546447744546663575533256334363365442622254523125255351333344334
232133113432234544554352242455426224355326625375457436577634474767555535546577656356574566466534733366642242352545631325212142555234442344213
134134243443235545413345331544664326536456355323773465564766375643547643734465565567755646666354425566664226646443325232215421344113231433424
311414212223243435443253441523422532533546652343233366467353367456765344677664436355635646542236522344226542526521331313325355112414212322421
334232443321214421211245451135156243663543242242266643734575556667574545756556643547337554242352425255443425263343355243143343221241214234343
124232141423143444334521514545324434424355644463624363327734476336434633435673465446464366334525462434632323446441521144323114143113241321322
321414331231141234351213225534114256365433422465655242455623675653343654456737676334562333232443533433345336621513331511453141434223121224422
233213212123332231444321554454521243352252556656534523664223224626544456453443223453642526535524426434322325222151553122432424133221432123312
132321423141322311111455511235131324533532253633455555424625245553424542362565522535443266232235665253526451221523231511534143214332442333423
231123343344444323131332211451353122524546266666363455365654343226336355324563455436265544334662333235265255142321144434543434214242441243332
111133423112214421432525544554514441143234656452524644342365355552246535242244443255664242362635265463654225515333115335451431434232224433122
233313113331334443314144235232155111242434354636364324664646444542553565524232453555263445434425533333113315152345245133213224312324131222222
122331314221321232244311154432354132551355214343635355633243553456534342552562224252264552632654646142443252452232455541422134411424133323213
321323232214143324412144152353142253333434221326622552645434535562666444426333326456265552323653322335233241235433141534442344442412141323122
333322211144143144413124114531254255313451244544546656322543634262532645655655636632423532352254234545251152154535241311224344244322132331111
233223131323341323132343132144124232445141442155112456324443652622633353344463432453352632231125552213124122311155413441434142413111222332332
323223212113232314444441311112512135441525235234551145264266223553444526342234456245465642135234421551443551533543133123214241222432213223122
311312332231134342414324333243224514535534312111323131434542623323632346523323446362131122522334552125245251413132113224314134423411111333331
331232112322123214133424214211315152511525535444441112554314211212133344544334245121341153154552255531251335211131123331322121233121311111123
112222313331221111442434111223431425412314322343135331535353312535342545315342221553551233455324225352231511444332413214443431341333321333323
113322121232321311434444342111232434555234332411453131314453234552423312521155444131243522241333531125233313122342413211344414121221321132123
231132131331212231143441111443414113444433535543534441452415315435355153145243235542533153124432435253444243321324133241144422333223322331123
122332113112121213234112443231334411112234351253542213533414315524215133522524342325151543155414215411524114144443322341233311111323322333113
""")