(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[38],{6730:function(e,t,o){"use strict";o.r(t),o.d(t,"default",(function(){return c}));var r=o(16),n=o(17),a=o(35),i=o(36),l=o(0),u=o.n(l),s=o(227),m=o(185),p=o(5),c=function(e){Object(a.a)(o,e);var t=Object(i.a)(o);function o(){var e;Object(r.a)(this,o);for(var n=arguments.length,a=new Array(n),i=0;i<n;i++)a[i]=arguments[i];return(e=t.call.apply(t,[this].concat(a))).formClearHelper=new s.b,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setStringValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onColorClose=function(t){e.setState({value:t},(function(){return e.commitWidgetValue({fromUi:!0})}))},e}return Object(n.a)(o,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"render",value:function(){var e=this.props,t=e.element,o=e.width,r=e.disabled,n=e.widgetMgr,a=this.state.value;return this.formClearHelper.manageFormClearListener(n,t.formId,this.onFormCleared),Object(p.jsx)(m.a,{label:t.label,help:t.help,onChange:this.onColorClose,disabled:r,width:o,value:a})}}]),o}(u.a.PureComponent)}}]);