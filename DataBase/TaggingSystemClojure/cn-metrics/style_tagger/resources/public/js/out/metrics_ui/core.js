// Compiled by ClojureScript 0.0-3308 {}
goog.provide('metrics_ui.core');
goog.require('cljs.core');
goog.require('reagent.core');
goog.require('ajax.core');
goog.require('secretary.core');
goog.require('reagent.session');
goog.require('goog.history.EventType');
goog.require('goog.History');
goog.require('goog.events');
metrics_ui.core.home_page = (function metrics_ui$core$home_page(){
return new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"h2","h2",-372662728),"Welcomeu to metrics-ui"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"a","a",-2123407586),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"href","href",-793805698),"#/about"], null),"go to about page"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"a","a",-2123407586),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"href","href",-793805698),"#/event"], null),"go to about page"], null)], null)], null);
});
metrics_ui.core.event_page = (function metrics_ui$core$event_page(){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"h2","h2",-372662728),"about events"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"a","a",-2123407586),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"href","href",-793805698),"#/"], null),"go to the home page"], null)], null)], null);
});
metrics_ui.core.about_page = (function metrics_ui$core$about_page(){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"h2","h2",-372662728),"About metrics-ui"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"a","a",-2123407586),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"href","href",-793805698),"#/"], null),"go to the home page"], null)], null)], null);
});
metrics_ui.core.current_page = (function metrics_ui$core$current_page(){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"div","div",1057191632),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [reagent.session.get.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180))], null)], null);
});
secretary.core.set_config_BANG_.call(null,new cljs.core.Keyword(null,"prefix","prefix",-265908465),"#");
var action__23694__auto___25879 = (function (params__23695__auto__){
if(cljs.core.map_QMARK_.call(null,params__23695__auto__)){
var map__25877 = params__23695__auto__;
var map__25877__$1 = ((cljs.core.seq_QMARK_.call(null,map__25877))?cljs.core.apply.call(null,cljs.core.hash_map,map__25877):map__25877);
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.home_page;},new cljs.core.Symbol("metrics-ui.core","home-page","metrics-ui.core/home-page",392510360,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"home-page","home-page",-850279575,null),"src/cljs/style_tagger/core.cljs",16,1,13,13,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.home_page)?metrics_ui.core.home_page.cljs$lang$test:null)])));
} else {
if(cljs.core.vector_QMARK_.call(null,params__23695__auto__)){
var vec__25878 = params__23695__auto__;
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.home_page;},new cljs.core.Symbol("metrics-ui.core","home-page","metrics-ui.core/home-page",392510360,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"home-page","home-page",-850279575,null),"src/cljs/style_tagger/core.cljs",16,1,13,13,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.home_page)?metrics_ui.core.home_page.cljs$lang$test:null)])));
} else {
return null;
}
}
});
secretary.core.add_route_BANG_.call(null,"/",action__23694__auto___25879);

var action__23694__auto___25882 = (function (params__23695__auto__){
if(cljs.core.map_QMARK_.call(null,params__23695__auto__)){
var map__25880 = params__23695__auto__;
var map__25880__$1 = ((cljs.core.seq_QMARK_.call(null,map__25880))?cljs.core.apply.call(null,cljs.core.hash_map,map__25880):map__25880);
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.about_page;},new cljs.core.Symbol("metrics-ui.core","about-page","metrics-ui.core/about-page",1221630104,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"about-page","about-page",2116788009,null),"src/cljs/style_tagger/core.cljs",17,1,22,22,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.about_page)?metrics_ui.core.about_page.cljs$lang$test:null)])));
} else {
if(cljs.core.vector_QMARK_.call(null,params__23695__auto__)){
var vec__25881 = params__23695__auto__;
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.about_page;},new cljs.core.Symbol("metrics-ui.core","about-page","metrics-ui.core/about-page",1221630104,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"about-page","about-page",2116788009,null),"src/cljs/style_tagger/core.cljs",17,1,22,22,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.about_page)?metrics_ui.core.about_page.cljs$lang$test:null)])));
} else {
return null;
}
}
});
secretary.core.add_route_BANG_.call(null,"/about",action__23694__auto___25882);

var action__23694__auto___25885 = (function (params__23695__auto__){
if(cljs.core.map_QMARK_.call(null,params__23695__auto__)){
var map__25883 = params__23695__auto__;
var map__25883__$1 = ((cljs.core.seq_QMARK_.call(null,map__25883))?cljs.core.apply.call(null,cljs.core.hash_map,map__25883):map__25883);
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.event_page;},new cljs.core.Symbol("metrics-ui.core","event-page","metrics-ui.core/event-page",-934720783,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"event-page","event-page",1044529826,null),"src/cljs/style_tagger/core.cljs",17,1,18,18,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.event_page)?metrics_ui.core.event_page.cljs$lang$test:null)])));
} else {
if(cljs.core.vector_QMARK_.call(null,params__23695__auto__)){
var vec__25884 = params__23695__auto__;
return reagent.session.put_BANG_.call(null,new cljs.core.Keyword(null,"current-page","current-page",-101294180),new cljs.core.Var(function(){return metrics_ui.core.event_page;},new cljs.core.Symbol("metrics-ui.core","event-page","metrics-ui.core/event-page",-934720783,null),cljs.core.PersistentHashMap.fromArrays([new cljs.core.Keyword(null,"ns","ns",441598760),new cljs.core.Keyword(null,"name","name",1843675177),new cljs.core.Keyword(null,"file","file",-1269645878),new cljs.core.Keyword(null,"end-column","end-column",1425389514),new cljs.core.Keyword(null,"column","column",2078222095),new cljs.core.Keyword(null,"line","line",212345235),new cljs.core.Keyword(null,"end-line","end-line",1837326455),new cljs.core.Keyword(null,"arglists","arglists",1661989754),new cljs.core.Keyword(null,"doc","doc",1913296891),new cljs.core.Keyword(null,"test","test",577538877)],[new cljs.core.Symbol(null,"metrics-ui.core","metrics-ui.core",883512900,null),new cljs.core.Symbol(null,"event-page","event-page",1044529826,null),"src/cljs/style_tagger/core.cljs",17,1,18,18,cljs.core.list(cljs.core.PersistentVector.EMPTY),null,(cljs.core.truth_(metrics_ui.core.event_page)?metrics_ui.core.event_page.cljs$lang$test:null)])));
} else {
return null;
}
}
});
secretary.core.add_route_BANG_.call(null,"/event",action__23694__auto___25885);

metrics_ui.core.hook_browser_navigation_BANG_ = (function metrics_ui$core$hook_browser_navigation_BANG_(){
var G__25887 = (new goog.History());
goog.events.listen(G__25887,goog.history.EventType.NAVIGATE,((function (G__25887){
return (function (event){
return secretary.core.dispatch_BANG_.call(null,event.token);
});})(G__25887))
);

G__25887.setEnabled(true);

return G__25887;
});
metrics_ui.core.mount_root = (function metrics_ui$core$mount_root(){
return reagent.core.render.call(null,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [metrics_ui.core.current_page], null),document.getElementById("app"));
});
metrics_ui.core.init_BANG_ = (function metrics_ui$core$init_BANG_(){
metrics_ui.core.hook_browser_navigation_BANG_.call(null);

return metrics_ui.core.mount_root.call(null);
});

//# sourceMappingURL=core.js.map