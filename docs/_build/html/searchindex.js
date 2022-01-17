Search.setIndex({docnames:["core","core.migrations","core.models","core.templatetags","core.views","index","manage","mg_tourism","modules","populate_db"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["core.rst","core.migrations.rst","core.models.rst","core.templatetags.rst","core.views.rst","index.rst","manage.rst","mg_tourism.rst","modules.rst","populate_db.rst"],objects:{"":[[0,0,0,"-","core"],[6,0,0,"-","manage"],[7,0,0,"-","mg_tourism"],[9,0,0,"-","populate_db"]],"core.apps":[[0,1,1,"","CoreConfig"]],"core.apps.CoreConfig":[[0,2,1,"","default_auto_field"],[0,2,1,"","name"],[0,3,1,"","ready"]],"core.decorators":[[0,4,1,"","is_plan_owner"]],"core.forms":[[0,1,1,"","PictureForm"],[0,1,1,"","UserProfileForm"]],"core.forms.PictureForm":[[0,1,1,"","Meta"],[0,2,1,"","base_fields"],[0,2,1,"","declared_fields"],[0,5,1,"","media"]],"core.forms.PictureForm.Meta":[[0,2,1,"","fields"],[0,2,1,"","model"]],"core.forms.UserProfileForm":[[0,1,1,"","Meta"],[0,2,1,"","base_fields"],[0,2,1,"","declared_fields"],[0,5,1,"","media"]],"core.forms.UserProfileForm.Meta":[[0,2,1,"","fields"],[0,2,1,"","model"]],"core.jobs":[[0,4,1,"","call_archive"],[0,4,1,"","run_continuously"],[0,4,1,"","start_scheduler"]],"core.migrations":[[1,0,0,"-","0001_initial"]],"core.migrations.0001_initial":[[1,1,1,"","Migration"]],"core.migrations.0001_initial.Migration":[[1,2,1,"","dependencies"],[1,2,1,"","initial"],[1,2,1,"","operations"]],"core.mixins":[[0,1,1,"","IsFirstComment"],[0,1,1,"","IsSuperuserMixin"],[0,1,1,"","IsTheCommentAuthor"],[0,1,1,"","IsThePlanOwner"],[0,1,1,"","IsTheUserMixin"]],"core.mixins.IsFirstComment":[[0,3,1,"","test_func"]],"core.mixins.IsSuperuserMixin":[[0,3,1,"","test_func"]],"core.mixins.IsTheCommentAuthor":[[0,3,1,"","test_func"]],"core.mixins.IsThePlanOwner":[[0,3,1,"","test_func"]],"core.mixins.IsTheUserMixin":[[0,3,1,"","test_func"]],"core.models":[[2,0,0,"-","comment"],[2,0,0,"-","plan"],[2,0,0,"-","thing"],[2,0,0,"-","user"]],"core.models.comment":[[2,1,1,"","Comment"]],"core.models.comment.Comment":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,2,1,"","author"],[2,2,1,"","author_id"],[2,2,1,"","content"],[2,3,1,"","get_absolute_url"],[2,3,1,"","get_next_by_posted_on"],[2,3,1,"","get_previous_by_posted_on"],[2,2,1,"","id"],[2,2,1,"","is_edited"],[2,2,1,"","objects"],[2,2,1,"","posted_on"],[2,2,1,"","rating"],[2,3,1,"","save"],[2,2,1,"","thing"],[2,2,1,"","thing_id"],[2,2,1,"","title"]],"core.models.plan":[[2,1,1,"","Plan"]],"core.models.plan.Plan":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,2,1,"","description"],[2,3,1,"","get_absolute_url"],[2,2,1,"","id"],[2,2,1,"","is_public"],[2,2,1,"","liked_by"],[2,2,1,"","name"],[2,2,1,"","objects"],[2,2,1,"","owner"],[2,2,1,"","owner_id"],[2,2,1,"","things"]],"core.models.thing":[[2,1,1,"","Attraction"],[2,1,1,"","Food"],[2,1,1,"","Outdoor"],[2,1,1,"","Picture"],[2,1,1,"","Shopping"],[2,1,1,"","Thing"],[2,1,1,"","Tour"]],"core.models.thing.Attraction":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,3,1,"","get_good_for_display"],[2,3,1,"","get_type_display"],[2,2,1,"","good_for"],[2,2,1,"","good_fors"],[2,2,1,"","neighborhood"],[2,2,1,"","thing_ptr"],[2,2,1,"","thing_ptr_id"],[2,2,1,"","tuple_choices"],[2,2,1,"","tuple_types"],[2,2,1,"","type"],[2,2,1,"","types"]],"core.models.thing.Food":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,3,1,"","get_good_for_display"],[2,3,1,"","get_type_display"],[2,2,1,"","good_for"],[2,2,1,"","good_fors"],[2,2,1,"","neighborhood"],[2,2,1,"","thing_ptr"],[2,2,1,"","thing_ptr_id"],[2,2,1,"","tuple_choices"],[2,2,1,"","tuple_types"],[2,2,1,"","type"],[2,2,1,"","types"]],"core.models.thing.Outdoor":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,3,1,"","get_good_for_display"],[2,3,1,"","get_type_display"],[2,2,1,"","good_for"],[2,2,1,"","good_fors"],[2,2,1,"","neighborhood"],[2,2,1,"","thing_ptr"],[2,2,1,"","thing_ptr_id"],[2,2,1,"","tuple_choices"],[2,2,1,"","tuple_types"],[2,2,1,"","type"],[2,2,1,"","types"]],"core.models.thing.Picture":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,3,1,"","get_absolute_url"],[2,2,1,"","id"],[2,2,1,"","image"],[2,2,1,"","objects"],[2,2,1,"","thing"],[2,2,1,"","thing_id"]],"core.models.thing.Shopping":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,3,1,"","get_good_for_display"],[2,3,1,"","get_type_display"],[2,2,1,"","good_for"],[2,2,1,"","good_fors"],[2,2,1,"","neighborhood"],[2,2,1,"","thing_ptr"],[2,2,1,"","thing_ptr_id"],[2,2,1,"","tuple_choices"],[2,2,1,"","tuple_types"],[2,2,1,"","type"],[2,2,1,"","types"]],"core.models.thing.Thing":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,2,1,"","address"],[2,2,1,"","attraction"],[2,2,1,"","categories"],[2,2,1,"","category"],[2,2,1,"","comments"],[2,2,1,"","covid_safe"],[2,2,1,"","food"],[2,3,1,"","get_absolute_url"],[2,3,1,"","get_category_display"],[2,3,1,"","get_fields"],[2,3,1,"","get_picture"],[2,2,1,"","id"],[2,2,1,"","long_description"],[2,2,1,"","name"],[2,2,1,"","objects"],[2,2,1,"","outdoor"],[2,2,1,"","pictures"],[2,2,1,"","plans_in"],[2,3,1,"","remove_unwanted_keys"],[2,2,1,"","shopping"],[2,2,1,"","short_description"],[2,2,1,"","stars"],[2,2,1,"","tour"],[2,2,1,"","tuple_categories"]],"core.models.thing.Tour":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,2,1,"","category"],[2,2,1,"","duration"],[2,3,1,"","get_type_display"],[2,2,1,"","price"],[2,2,1,"","thing_ptr"],[2,2,1,"","thing_ptr_id"],[2,2,1,"","tuple_types"],[2,2,1,"","type"],[2,2,1,"","types"]],"core.models.user":[[2,1,1,"","UserProfile"]],"core.models.user.UserProfile":[[2,6,1,"","DoesNotExist"],[2,6,1,"","MultipleObjectsReturned"],[2,2,1,"","biography"],[2,2,1,"","comments"],[2,3,1,"","get_absolute_url"],[2,2,1,"","liked"],[2,2,1,"","plans"],[2,2,1,"","profile_pic"],[2,2,1,"","user_ptr"],[2,2,1,"","user_ptr_id"]],"core.templatetags":[[3,0,0,"-","my_filters"],[3,0,0,"-","my_tags"]],"core.templatetags.my_filters":[[3,4,1,"","add_spaces"],[3,4,1,"","make_possessive"],[3,4,1,"","to_int"],[3,4,1,"","to_str"]],"core.templatetags.my_tags":[[3,4,1,"","any_query"],[3,4,1,"","any_tab_selected"],[3,4,1,"","get_all_things"],[3,4,1,"","get_field_value"],[3,4,1,"","get_good_fors"],[3,4,1,"","get_owner"],[3,4,1,"","get_param_value"],[3,4,1,"","get_plans"],[3,4,1,"","get_thing"],[3,4,1,"","get_top_plans"],[3,4,1,"","get_top_things"],[3,4,1,"","get_types"],[3,4,1,"","get_visible_plans"],[3,4,1,"","is_checked"],[3,4,1,"","is_in_query"],[3,4,1,"","is_tab_selected"],[3,4,1,"","user_commented"],[3,4,1,"","user_liked"]],"core.views":[[4,0,0,"-","comment"],[4,0,0,"-","index"],[4,0,0,"-","picture"],[4,0,0,"-","plan"],[4,0,0,"-","thing"],[4,0,0,"-","thing_create"],[4,0,0,"-","user"]],"core.views.comment":[[4,1,1,"","CommentCreateView"],[4,1,1,"","CommentDeleteView"],[4,1,1,"","CommentUpdateView"]],"core.views.comment.CommentCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.comment.CommentDeleteView":[[4,3,1,"","get_success_url"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.comment.CommentUpdateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.index":[[4,1,1,"","DocsView"],[4,1,1,"","FeaturesView"],[4,1,1,"","IndexView"]],"core.views.index.DocsView":[[4,2,1,"","template_name"]],"core.views.index.FeaturesView":[[4,2,1,"","template_name"]],"core.views.index.IndexView":[[4,2,1,"","template_name"]],"core.views.picture":[[4,1,1,"","PictureCreateView"]],"core.views.picture.PictureCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"]],"core.views.plan":[[4,1,1,"","PlanCreateView"],[4,1,1,"","PlanDeleteView"],[4,1,1,"","PlanUpdateView"],[4,4,1,"","plan_like"]],"core.views.plan.PlanCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,3,1,"","get_success_url"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.plan.PlanDeleteView":[[4,3,1,"","get_success_url"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.plan.PlanUpdateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing":[[4,1,1,"","ThingDeleteView"],[4,1,1,"","ThingDetailView"],[4,1,1,"","ThingListView"],[4,1,1,"","ThingUpdateView"]],"core.views.thing.ThingDeleteView":[[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","success_url"],[4,2,1,"","template_name"]],"core.views.thing.ThingDetailView":[[4,2,1,"","context_object_name"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing.ThingListView":[[4,3,1,"","combine"],[4,3,1,"","get"],[4,3,1,"","get_cat_dependent_filters"],[4,3,1,"","get_cat_independent_filters"],[4,3,1,"","get_context_data"],[4,3,1,"","get_query_categories"],[4,3,1,"","get_query_fields"],[4,3,1,"","get_queryset"],[4,2,1,"","model"],[4,3,1,"","query_filter_fields"],[4,2,1,"","template_name"]],"core.views.thing.ThingUpdateView":[[4,2,1,"","fields"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing_create":[[4,1,1,"","AttractionCreateView"],[4,1,1,"","FoodCreateView"],[4,1,1,"","OutdoorCreateView"],[4,1,1,"","ShoppingCreateView"],[4,1,1,"","TourCreateView"]],"core.views.thing_create.AttractionCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing_create.FoodCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing_create.OutdoorCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing_create.ShoppingCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.thing_create.TourCreateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.user":[[4,1,1,"","UserDeleteView"],[4,1,1,"","UserDetailView"],[4,1,1,"","UserUpdateView"],[4,4,1,"","register"],[4,4,1,"","user_login"],[4,4,1,"","user_logout"]],"core.views.user.UserDeleteView":[[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","success_url"],[4,2,1,"","template_name"]],"core.views.user.UserDetailView":[[4,2,1,"","context_object_name"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"core.views.user.UserUpdateView":[[4,2,1,"","fields"],[4,3,1,"","form_valid"],[4,2,1,"","login_url"],[4,2,1,"","model"],[4,2,1,"","template_name"]],"populate_db.FakeCommentGenerator":[[9,3,1,"","create"],[9,3,1,"","generate"]],"populate_db.FakePlanGenerator":[[9,3,1,"","add_likes"],[9,3,1,"","add_things"],[9,3,1,"","create"],[9,3,1,"","generate"]],"populate_db.FakeThingGenerator":[[9,3,1,"","add_pics"],[9,3,1,"","download_thing_pic"],[9,3,1,"","generate"],[9,3,1,"","generate_attraction_specific_fields"],[9,3,1,"","generate_food_specific_fields"],[9,3,1,"","generate_outdoor_specific_fields"],[9,3,1,"","generate_shopping_specific_fields"],[9,3,1,"","generate_thing_fields"],[9,3,1,"","generate_tour_specific_fields"],[9,3,1,"","get_address"],[9,3,1,"","get_choices"],[9,2,1,"","neighborhoods"]],"populate_db.FakeUserGenerator":[[9,3,1,"","create"],[9,3,1,"","generate"]],core:[[0,0,0,"-","admin"],[0,0,0,"-","apps"],[0,0,0,"-","decorators"],[0,0,0,"-","forms"],[0,0,0,"-","jobs"],[1,0,0,"-","migrations"],[0,0,0,"-","mixins"],[2,0,0,"-","models"],[3,0,0,"-","templatetags"],[0,0,0,"-","urls"],[4,0,0,"-","views"]],manage:[[6,4,1,"","main"]],mg_tourism:[[7,0,0,"-","asgi"],[7,0,0,"-","settings"],[7,0,0,"-","urls"],[7,0,0,"-","wsgi"]],populate_db:[[9,1,1,"","FakeCommentGenerator"],[9,1,1,"","FakePlanGenerator"],[9,1,1,"","FakeThingGenerator"],[9,1,1,"","FakeUserGenerator"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","method","Python method"],"4":["py","function","Python function"],"5":["py","property","Python property"],"6":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:method","4":"py:function","5":"py:property","6":"py:exception"},terms:{"0":7,"0001_initi":[0,8],"0012_alter_user_first_name_max_length":1,"1":0,"10":9,"12":9,"1280":9,"2":9,"3":[3,9],"30":9,"4":[3,7],"403":0,"44896618":0,"44897678":0,"5":9,"500":9,"60":9,"7":9,"720":9,"abstract":1,"bet\u00e2nia":9,"class":[0,1,2,4,7,9],"do":[0,9],"float":3,"function":[0,3,7],"import":7,"in\u00ea":9,"int":[0,3,4,9],"jos\u00e9":9,"new":2,"para\u00edso":9,"public":4,"return":[0,2,3,4,9],"ros\u00e1rio":9,"s\u00e3o":9,"static":[4,9],"switch":3,"true":[1,2],A:2,For:7,If:4,In:2,It:7,The:[2,4,7],Will:0,access:[0,4],accessor:2,activ:3,ad:3,add:[7,9],add_lik:9,add_pic:9,add_spac:3,add_th:9,address:[1,2,4,9],admin:[7,8],administr:6,adrenalin:2,after:4,alia:[0,4],all:[0,3,4],allow:3,alreadi:[0,4],amount:9,an:[3,7,9],ani:[2,3,4,9],anoth:[4,7],antiqu:2,any_queri:3,any_tab_select:3,apostroph:3,app:8,app_label:1,app_modul:0,app_nam:0,appconfig:0,applic:7,appropri:[2,3,4],ar:[0,2,3,4],archiv:0,arg:[2,4],as_view:7,asgi:8,assign:2,associ:[0,3,4],attract:[1,2,4],attractioncreateview:4,attribut:[0,4,9],auth:[0,1,2,4],author:[0,1,2,4],author_id:2,auto_id:0,avail:3,averag:2,back:4,backup:0,bacurau:9,bar:2,base:[0,1,2,4,7,9],base_field:0,basic:4,becaus:4,being:3,below:2,big:2,bigautofield:[0,1],bike:2,biographi:[0,1,2,4],biography_length:9,blog:7,bool:[0,3],booleanfield:1,bosco:9,brazil:9,breweri:2,built:2,call_arch:0,callabl:[0,7],can:[0,3],capit:3,categori:[1,2,3,4,9],chang:3,charfield:[0,1,2],check:[0,3,4],child:[2,9],children:[2,4,9],choic:9,chosen:9,citi:2,code:0,coffe:2,com:[0,7],combin:4,come:4,command:[0,6],comment:[0,1,3,8,9],commentcreateview:4,commentdeleteview:4,commentupdateview:4,config:[0,7],configur:7,confirm_delet:4,content:8,context_object_nam:4,contrib:[0,1,2,4],convert:3,core:[5,8,9],coreconfig:0,count:3,coupl:2,covid_saf:[1,2,4],creat:[2,4,9],create_forward_many_to_many_manag:2,createmodel:1,createview:[0,4],creation:4,crispi:0,crispy_form:0,cultur:2,custom:3,dai:[0,2],data:[0,9],databas:[0,9],date_join:2,datefield:[1,2],db:[0,1,2,3,4],decimalfield:1,declared_field:0,decor:8,default_auto_field:0,defer:2,defin:2,deleg:2,delet:4,deleteview:4,deni:0,depart:2,depend:[1,3,4],deploy:7,descript:[1,2,4],description_length:9,detail:[3,4],detailview:4,determin:4,dict:[2,3,4,9],dictionari:4,differ:2,diliks:4,dislik:4,displai:[3,4],django:[0,1,2,3,4,6,7],django_arch:0,djangoproject:7,doc:[4,7],docsview:4,document:[],doesnotexist:2,dom:9,download:9,download_thing_p:9,durat:[1,2,4],durationfield:1,dynam:[0,2],each:9,edit:4,els:4,email:[0,2,4],emailfield:0,empti:3,empty_permit:0,en:[0,7],error:0,error_class:0,errorlist:0,even:3,event:0,everi:[0,3,9],exampl:[2,7],except:[2,4],execut:2,explor:2,expos:7,factori:2,fake:9,fake_profile_p:9,fakecommentgener:9,fakeplangener:9,fakethinggener:9,fakeusergener:9,fals:[0,1,2],farmer:2,featur:4,featuresview:4,field:[0,1,2,3,4,9],file:[0,1,7],filedescriptor:2,filenam:9,filter:[3,4],first:2,first_nam:[0,2,4],fit:4,food:[1,2,4,9],foodcreateview:4,forbidden:0,foreignkei:[1,2],form:[4,8],form_valid:4,format:3,fors:3,forward:2,forwardmanytoonedescriptor:2,forwardonetoonedescriptor:2,francisco:9,from:[0,2,4,7],full:7,fun:2,gener:[4,7,9],generate_attraction_specific_field:9,generate_food_specific_field:9,generate_outdoor_specific_field:9,generate_shopping_specific_field:9,generate_thing_field:9,generate_tour_specific_field:9,gerai:9,get:[3,4,9],get_absolute_url:2,get_address:9,get_all_th:3,get_cat_dependent_filt:4,get_cat_independent_filt:4,get_category_displai:2,get_choic:9,get_context_data:4,get_field:2,get_field_valu:3,get_good_for:3,get_good_for_displai:2,get_next_by_posted_on:2,get_own:3,get_param_valu:3,get_pictur:2,get_plan:3,get_previous_by_posted_on:2,get_query_categori:4,get_query_field:4,get_queryset:4,get_success_url:4,get_th:3,get_top_plan:3,get_top_th:3,get_typ:3,get_type_displai:2,get_visible_plan:3,gift:2,given:[3,4],good:3,good_for:[1,2,4],group:2,ha:[0,3,4],have:0,height:2,height_field:2,hike:2,histor:2,home:7,howto:7,html:4,http:[0,4,7,9],httprespons:4,i:4,id:[1,2],id_:0,imag:[0,1,2,4,9],imagefield:[0,1,2],img:9,implement:2,includ:[0,7],independ:[2,3,4],index:[0,5,8],indexview:4,inform:7,initi:[0,1],input:4,instanc:[0,2],integ:3,interv:0,io:0,is_act:2,is_check:3,is_edit:[1,2,4],is_in_queri:3,is_next:2,is_plan_own:0,is_publ:[1,2,4],is_staff:2,is_superus:2,is_tab_select:3,isfirstcom:[0,4],issuperusermixin:[0,4],isthecommentauthor:[0,4],istheplanown:[0,4],istheus:[],istheusermixin:[0,4],its:[2,3],jardim:9,job:8,jona:9,jpg:9,just:2,kid:2,kwarg:[2,4],label_suffix:0,landmark:2,last_login:2,last_nam:[0,2,4],latest:0,level:7,like:[2,3,4],liked_bi:[1,2,9],line:6,link:4,list:[3,4,7],listview:4,load:2,log:0,login:4,login_url:[0,4],loginrequiredmixin:[0,4],logout:4,long_descript:[1,2,4],long_description_length:9,longer:4,look:3,main:[3,6],make:3,make_possess:3,mall:2,manag:[1,2,5,8],mani:2,manual:4,manytomanydescriptor:2,manytomanyfield:[1,2],market:2,match:4,matchin:4,max_dur:9,max_n:9,max_pric:9,media:0,meta:0,method:0,mg_tourism:5,midnight:0,migrat:[0,8],min_dur:9,min_pric:9,mina:9,mixin:[4,8],model:[0,1,3,4,8,9],modelform:0,modul:[5,8],monica:9,more:7,most:[2,4],multi:2,multipleobjectsreturn:2,museum:2,my:4,my_app:7,my_filt:[0,8],my_tag:[0,8],n:9,name:[0,1,2,3,4,7],need:4,neighborhood:[1,2,4,9],next:4,nightlif:2,none:[0,2,3,9],nossa:9,number:9,object:[0,1,2,3,4,9],objectdoesnotexist:2,one:[2,4],ones:0,onetoonefield:[1,2],onli:[2,4],oper:1,option:1,other:3,other_app:7,outdoor:[1,2,4,9],outdoorcreateview:4,outlet:2,overrid:0,own:4,owner:[0,1,2,3,4],owner_id:2,packag:[5,8],page:[0,4,5],param:3,paramet:[3,4],paremet:[],parent:2,password:[0,2],path:[7,9],permissiondeni:0,photo:9,picsum:9,pictur:[0,1,2,8,9],picturecreateview:4,pictureform:0,pizza:2,pk:[3,4],place:2,plan:[0,1,3,8,9],plan_lik:4,plan_pk:[3,4],plancreateview:4,plandeleteview:4,plans_in:2,planupdateview:4,pleas:7,populate_db:[5,8],possess:3,possibl:[3,9],post:[0,4],posted_on:[1,2],prefix:0,price:[1,2,4],privat:[2,3],profil:[4,9],profile_p:[0,1,2,4],profile_pics_path:9,project:[4,7],properti:0,purpos:3,queri:[2,3,4],query_categori:4,query_field:4,query_filter_field:4,queryset:[3,4],querystr:4,question:0,raft:2,raini:2,rais:0,random:[2,9],randomli:9,rate:[1,2,4],read:2,readi:0,readthedoc:0,redirect:[0,4],ref:7,regist:4,relat:[1,2],related_nam:2,remov:[2,4],remove_unwanted_kei:2,render:0,replac:3,request:4,requir:0,respons:4,restaur:2,revers:2,reversemanytoonedescriptor:2,reverseonetoonedescriptor:2,river:2,rout:7,run:[0,6],run_continu:0,s:[0,3,4,6,9],santa:9,satisfi:4,save:[2,4],search:5,second:0,see:[4,7],seeker:2,select_filt:3,self:0,send:4,senhora:9,set:[4,8],shop:[1,2,4,9],shoppingcreateview:4,short_descript:[1,2,4],short_description_length:9,side:2,sight:2,similar:0,smallintegerfield:1,sourc:0,space:3,specif:[2,3,9],stackoverflow:0,star:[1,2],start:0,start_schedul:0,startproject:7,state:9,store:2,str:[2,3,4,9],string:3,subclass:[0,2],submodul:8,subpackag:8,success_url:4,superus:0,suppos:4,tab:[3,4],tag:3,task:6,templat:[3,4],template_nam:4,templatetag:[0,8],templateview:4,test_func:0,textfield:1,than:3,thei:[0,3,4],them:4,thi:[0,2,4,7],thinb:[],thing:[0,1,3,8,9],thing_creat:[0,8],thing_detail:4,thing_form:4,thing_id:2,thing_list:[2,4],thing_pk:3,thing_ptr:[1,2],thing_ptr_id:2,thingdeleteview:4,thingdetailview:4,thinglistview:4,thingupdateview:4,thread:0,time:[2,4],titl:[1,2,4],to_int:3,to_str:3,top:[2,3],topic:7,tour:[1,2,4,9],tourcreateview:4,tupl:9,tuple_categori:2,tuple_choic:2,tuple_typ:2,type:[1,2,3,4],underscor:3,union:3,uniqu:9,unwant:2,updat:[2,4],updateview:[0,4],url:[4,8,9],urlconf:7,urlpattern:7,us:[0,2,3,4,7],use_required_attribut:0,user:[0,1,3,8,9],user_com:3,user_detail:4,user_detail_pk:3,user_lik:3,user_login:4,user_logout:4,user_pk:3,user_ptr:[1,2],user_ptr_id:2,user_viewing_pk:3,userdeleteview:4,userdetailview:4,usermanag:1,usernam:[0,2,4],userpassestestmixin:0,userprofil:[0,1,2,3,4,9],userprofileform:0,userupdateview:4,usual:3,util:[0,6],valid:[0,4],valu:[2,3,4,7,9],variabl:[4,7],veiga:9,verbose_nam:1,verbose_name_plur:1,via:2,view:[0,3,7,8],vila:9,visit:3,wai:0,wether:3,when:[0,2],which:4,widget:0,width:2,width_field:2,wildlif:2,wine:2,within:[3,4],word:3,wrapper:2,wsgi:8,x:0,zoo:2},titles:["core package","core.migrations package","core.models package","core.templatetags package","core.views package","Welcome to MG Tourism\u2019s documentation!","manage module","mg_tourism package","mg_tourism","populate_db module"],titleterms:{"0001_initi":1,admin:0,app:0,asgi:7,comment:[2,4],content:[0,1,2,3,4,5,7],core:[0,1,2,3,4],decor:0,document:5,form:0,index:4,indic:5,job:0,manag:6,mg:5,mg_tourism:[7,8],migrat:1,mixin:0,model:2,modul:[0,1,2,3,4,6,7,9],my_filt:3,my_tag:3,packag:[0,1,2,3,4,7],pictur:4,plan:[2,4],populate_db:9,s:5,set:7,submodul:[0,1,2,3,4,7],subpackag:0,tabl:5,templatetag:3,thing:[2,4],thing_creat:4,tourism:5,url:[0,7],user:[2,4],view:4,welcom:5,wsgi:7}})