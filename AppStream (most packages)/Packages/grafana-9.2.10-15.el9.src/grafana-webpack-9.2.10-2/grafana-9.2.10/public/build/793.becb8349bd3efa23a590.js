"use strict";(self.webpackChunkgrafana=self.webpackChunkgrafana||[]).push([[793],{11617:(e,a,t)=>{t.d(a,{j:()=>u});var n,s=t(77813),r=t(76687),i=t(27668),l=t(55312),o=t(62533),c=t(39756),d=t(96029),p=t(52010);const u=e=>{let{onChange:a,maxMenuHeight:t}=e;const s=(0,r.useMemo)((()=>(0,d.x)()),[]),u=(0,r.useMemo)((()=>s.map((e=>({label:e.name,imgUrl:e.info.logos.small,value:e}))).sort(((e,a)=>{var t;return null===(t=e.label)||void 0===t?void 0:t.localeCompare(a.label)}))),[s]),[h,m]=(0,r.useState)([]),x=(0,r.useCallback)((e=>{const t=e.filter((e=>e.value)).map((e=>e.value));a(t),m(e)}),[a]),f=(0,i.wW)(g),b={defaultOptions:!0,getOptionLabel:e=>e.label,getOptionValue:e=>e.value,noOptionsMessage:"No Panel types found",placeholder:"Filter by type",maxMenuHeight:t,options:u,value:h,onChange:x};return(0,p.jsxs)("div",{className:f.container,children:[h.length>0&&(0,p.jsx)(l.zx,{size:"xs",icon:"trash-alt",fill:"text",className:f.clear,onClick:()=>x([]),"aria-label":"Clear types",children:"Clear types"}),(0,p.jsx)(o.NU,Object.assign({},b,{prefix:n||(n=(0,p.jsx)(c.J,{name:"filter"})),"aria-label":"Panel Type filter"}))]})};function g(e){return{container:s.css`
      label: container;
      position: relative;
      min-width: 180px;
      flex-grow: 1;
    `,clear:s.css`
      label: clear;
      font-size: ${e.spacing(1.5)};
      position: absolute;
      top: -${e.spacing(4.5)};
      right: 0;
    `}}},80636:(e,a,t)=>{t.d(a,{p:()=>O});var n=t(77813),s=t(76687),r=t(67273),i=t(27668),l=t(39756),o=t(95296),c=t(50279),d=t(973),p=t(77212),u=t(99397),g=t(55312),h=t(60105),m=t(67225),x=t(79877),f=t(84890);const b={loadingState:p.Gu.Loading,dashboardTitles:[]},y=(0,f.PH)("libraryPanels/delete/searchCompleted"),v=function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:b,a=arguments.length>1?arguments[1]:void 0;return y.match(a)?Object.assign({},e,{dashboardTitles:a.payload.dashboards.map((e=>e.title)),loadingState:p.Gu.Done}):e};var w,j,C,P,$=t(52010);const S=e=>{let{libraryPanel:a,onDismiss:t,onConfirm:n}=e;const r=(0,i.yK)(h.J),[{dashboardTitles:l,loadingState:o},c]=(0,s.useReducer)(v,b),d=(0,s.useMemo)((()=>(0,m.tb)(c)),[c]);(0,s.useEffect)((()=>{d(function(e){return async function(a){const t=await(0,x.E8)(e.uid);a(y({dashboards:t}))}}(a))}),[d,a]);const f=Boolean(l.length),C=o===p.Gu.Done;return(0,$.jsxs)(u.u,{className:r.modal,title:"Delete library panel",icon:"trash-alt",onDismiss:t,isOpen:!0,children:[C?null:w||(w=(0,$.jsx)(k,{})),C?(0,$.jsxs)("div",{children:[f?(0,$.jsx)(F,{dashboardTitles:l}):null,f?null:j||(j=(0,$.jsx)(N,{})),(0,$.jsxs)(u.u.ButtonRow,{children:[(0,$.jsx)(g.zx,{variant:"secondary",onClick:t,fill:"outline",children:"Cancel"}),(0,$.jsx)(g.zx,{variant:"destructive",onClick:n,disabled:f,children:"Delete"})]})]}):null]})},k=()=>C||(C=(0,$.jsx)("span",{children:"Loading library panel..."})),N=()=>{const e=(0,i.yK)(h.J);return(0,$.jsx)("div",{className:e.modalText,children:"Do you want to delete this panel?"})},F=e=>{let{dashboardTitles:a}=e;const t=(0,i.yK)(h.J),n=1===a.length?"dashboard.":"dashboards.",s=`${a.length} ${n}`;return 0===a.length?null:(0,$.jsxs)("div",{children:[(0,$.jsxs)("p",{className:t.textInfo,children:["This library panel can not be deleted because it is connected to ",(0,$.jsx)("strong",{children:s})," Remove the library panel from the dashboards listed below and retry."]}),(0,$.jsxs)("table",{className:t.myTable,children:[P||(P=(0,$.jsx)("thead",{children:(0,$.jsx)("tr",{children:(0,$.jsx)("th",{children:"Dashboard name"})})})),(0,$.jsx)("tbody",{children:a.map(((e,a)=>(0,$.jsx)("tr",{children:(0,$.jsx)("td",{children:e})},`dash-title-${a}`)))})]})]})};var z,D;const O=e=>{var a;let{libraryPanel:t,onClick:n,onDelete:i,showSecondaryActions:l}=e;const[o,p]=(0,s.useState)(!1),u=null!==(a=r.v.panels[t.model.type])&&void 0!==a?a:(0,c.X)(t.model.type).meta;return(0,$.jsxs)($.Fragment,{children:[(0,$.jsx)(d.X,{isCurrent:!1,title:t.name,description:t.description,plugin:u,onClick:()=>null==n?void 0:n(t),onDelete:l?()=>p(!0):void 0,children:(0,$.jsx)(T,{libraryPanel:t})}),o&&(0,$.jsx)(S,{libraryPanel:t,onConfirm:()=>{null==i||i(t),p(!1)},onDismiss:()=>p(!1)})]})};function T(e){let{libraryPanel:a}=e;const t=(0,i.wW)(B);return a.meta.folderUid||a.meta.folderName?a.meta.folderUid?(0,$.jsx)("span",{className:t.metaContainer,children:(0,$.jsxs)(o.r,{href:`/dashboards/f/${a.meta.folderUid}`,children:[D||(D=(0,$.jsx)(l.J,{name:"folder-upload",size:"sm"})),(0,$.jsx)("span",{children:a.meta.folderName})]})}):(0,$.jsxs)("span",{className:t.metaContainer,children:[z||(z=(0,$.jsx)(l.J,{name:"folder",size:"sm"})),(0,$.jsx)("span",{children:a.meta.folderName})]}):null}function B(e){return{metaContainer:n.css`
      display: flex;
      align-items: center;
      color: ${e.colors.text.secondary};
      font-size: ${e.typography.bodySmall.fontSize};
      padding-top: ${e.spacing(.5)};

      svg {
        margin-right: ${e.spacing(.5)};
        margin-bottom: 3px;
      }
    `}}},90793:(e,a,t)=>{t.d(a,{N:()=>S,e:()=>$});var n,s=t(77813),r=t(76687),i=t(93308),l=t(27668),o=t(7053),c=t(3357),d=t(97368),p=t.n(d),u=t(55312),g=t(62533),h=t(39756),m=t(75477),x=t(98335),f=t(352),b=t(52010);function y(e){let{onChange:a,maxMenuHeight:t}=e;const s=(0,l.wW)(v),[i,o]=(0,r.useState)(!1),c=(0,r.useCallback)((e=>async function(e,a){a(!0);const t={query:e,type:x.o.DashFolder,permission:f.bf.View},n=(await(0,m.i)().search(t)).map((e=>({label:e.title,value:{id:e.id,title:e.title}})));e&&!"general".includes(e.toLowerCase())||n.unshift({label:"General",value:{id:0,title:"General"}});return a(!1),n}(e,o)),[]),d=(0,r.useMemo)((()=>p()(c,300)),[c]),[y,w]=(0,r.useState)([]),j=(0,r.useCallback)((e=>{const t=e.filter((e=>Boolean(e.value))).map((e=>e.value));a(t),w(e)}),[a]);return(0,b.jsxs)("div",{className:s.container,children:[y.length>0&&(0,b.jsx)(u.zx,{size:"xs",icon:"trash-alt",fill:"text",className:s.clear,onClick:()=>a([]),"aria-label":"Clear folders",children:"Clear folders"}),(0,b.jsx)(g.M8,{value:y,onChange:j,isLoading:i,loadOptions:d,maxMenuHeight:t,placeholder:"Filter by folder",noOptionsMessage:"No folders found",prefix:n||(n=(0,b.jsx)(h.J,{name:"filter"})),"aria-label":"Folder filter",defaultOptions:!0})]})}function v(e){return{container:s.css`
      label: container;
      position: relative;
      min-width: 180px;
      flex-grow: 1;
    `,clear:s.css`
      label: clear;
      font-size: ${e.spacing(1.5)};
      position: absolute;
      top: -${e.spacing(4.5)};
      right: 0;
    `}}var w=t(11617),j=t(4321),C=t(56921),P=t(61746);let $;!function(e){e.Tight="tight",e.Spacious="spacious"}($||($={}));const S=e=>{let{onClick:a,variant:t=$.Spacious,currentPanelId:n,currentFolderId:d,perPage:p=C.gN,showPanelFilter:u=!1,showFolderFilter:g=!1,showSort:h=!1,showSecondaryActions:m=!1}=e;const x=(0,l.wW)((0,r.useCallback)((e=>function(e,a){const t=s.css`
    flex-direction: row;
    row-gap: ${e.spacing(1)};
  `;return{filterInputWrapper:s.css`
      flex-grow: ${a===$.Tight?1:"initial"};
    `,container:s.css`
      width: 100%;
      overflow-y: auto;
      padding: ${e.spacing(1)};
    `,libraryPanelsView:s.css`
      width: 100%;
    `,gridContainer:s.css`
      ${a===$.Tight?t:""};
      display: flex;
      flex-direction: column;
      width: 100%;
      column-gap: ${e.spacing(1)};
      row-gap: ${e.spacing(1)};
      padding-bottom: ${e.spacing(2)};
    `}}(e,t)),[t])),[f,y]=(0,r.useState)(""),[v,w]=(0,r.useState)("");(0,i.Z)((()=>w(f)),200,[f]);const[j,S]=(0,r.useState)({}),[N,F]=(0,r.useState)(d?[String(d)]:[]),[z,D]=(0,r.useState)([]),O=h||u||g,T=t===$.Tight?"lg":"xs";return(0,b.jsx)("div",{className:x.container,children:(0,b.jsxs)(o.wc,{spacing:T,children:[(0,b.jsxs)("div",{className:x.gridContainer,children:[(0,b.jsx)("div",{className:x.filterInputWrapper,children:(0,b.jsx)(c.H,{value:f,onChange:y,placeholder:"Search by name or description",width:0,escapeRegex:!1})}),O&&(0,b.jsx)(k,{showSort:h,showPanelFilter:u,showFolderFilter:g,onSortChange:S,onFolderFilterChange:F,onPanelFilterChange:D,sortDirection:j.value,variant:t})]}),(0,b.jsx)("div",{className:x.libraryPanelsView,children:(0,b.jsx)(P.u,{onClickCard:a,searchString:v,sortDirection:j.value,panelFilter:z,folderFilter:N,currentPanelId:n,showSecondaryActions:m,perPage:p})})]})})};const k=r.memo((e=>{let{variant:a=$.Spacious,showSort:t,showPanelFilter:n,showFolderFilter:i,sortDirection:o,onSortChange:c,onFolderFilterChange:d,onPanelFilterChange:p}=e;const u=(0,l.wW)((0,r.useCallback)((e=>function(e){let a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:$.Spacious;const t=s.css`
    display: flex;
    gap: ${e.spacing(1)};
    flex-grow: 1;
    flex-direction: row;
    justify-content: end;
  `,n=s.css`
    ${t};
    flex-grow: initial;
    flex-direction: column;
    justify-content: normal;
  `,r=s.css`
    display: flex;
    flex-direction: row;
    margin-left: auto;
    gap: 4px;
  `,i=s.css`
    ${r};
    flex-direction: column;
    margin-left: initial;
  `;switch(a){case $.Spacious:return{container:t,filterContainer:r};case $.Tight:return{container:n,filterContainer:i}}}(e,a)),[a])),g=(0,r.useCallback)((e=>p(e.map((e=>e.id)))),[p]),h=(0,r.useCallback)((e=>d(e.map((e=>String(e.id))))),[d]);return(0,b.jsxs)("div",{className:u.container,children:[t&&(0,b.jsx)(j.P,{value:o,onChange:c,filter:["alpha-asc","alpha-desc"]}),(i||n)&&(0,b.jsxs)("div",{className:u.filterContainer,children:[i&&(0,b.jsx)(y,{onChange:h}),n&&(0,b.jsx)(w.j,{onChange:g})]})]})}));k.displayName="SearchControls"},61746:(e,a,t)=>{t.d(a,{u:()=>h});var n,s=t(77813),r=t(76687),i=t(93308),l=t(77212),o=t(27668),c=t(3526),d=t(80636),p=t(67225),u=t(94055),g=t(52010);const h=e=>{let{className:a,onClickCard:t,searchString:h,sortDirection:x,panelFilter:f,folderFilter:b,showSecondaryActions:y,currentPanelId:v,perPage:w=40}=e;const j=(0,o.yK)(m),[{libraryPanels:C,page:P,perPage:$,numberOfPages:S,loadingState:k,currentPanelId:N},F]=(0,r.useReducer)(u._p,Object.assign({},u.p$,{currentPanelId:v,perPage:w})),z=(0,r.useMemo)((()=>(0,p.tb)(F)),[F]);(0,i.Z)((()=>z((0,p.Xu)({searchString:h,sortDirection:x,panelFilter:f,folderFilter:b,page:P,perPage:$,currentPanelId:N}))),300,[h,x,f,b,P,z]);const D=e=>{let{uid:a}=e;return z((0,p.UO)(a,{searchString:h,page:P,perPage:$}))};return(0,g.jsxs)("div",{className:(0,s.cx)(j.container,a),children:[(0,g.jsx)("div",{className:j.libraryPanelList,children:k===l.Gu.Loading?n||(n=(0,g.jsx)("p",{children:"Loading library panels..."})):C.length<1?(0,g.jsx)("p",{className:j.noPanelsFound,children:"No library panels found."}):null==C?void 0:C.map(((e,a)=>(0,g.jsx)(d.p,{libraryPanel:e,onDelete:D,onClick:t,showSecondaryActions:y},`library-panel=${a}`)))}),C.length?(0,g.jsx)("div",{className:j.pagination,children:(0,g.jsx)(c.t,{currentPage:P,numberOfPages:S,onNavigate:e=>z((0,u.oO)({page:e})),hideWhenSinglePage:!0})}):null]})},m=e=>({container:s.css`
      display: flex;
      flex-direction: column;
      flex-wrap: nowrap;
    `,libraryPanelList:s.css`
      max-width: 100%;
      display: grid;
      grid-gap: ${e.spacing.sm};
    `,searchHeader:s.css`
      display: flex;
    `,newPanelButton:s.css`
      margin-top: 10px;
      align-self: flex-start;
    `,pagination:s.css`
      align-self: center;
      margin-top: ${e.spacing.sm};
    `,noPanelsFound:s.css`
      label: noPanelsFound;
      min-height: 200px;
    `})},67225:(e,a,t)=>{t.d(a,{UO:()=>f,Xu:()=>x,tb:()=>b});var n=t(18919),s=t(23280),r=t(98800),i=t(47894),l=t(16649),o=t(2670),c=t(95481),d=t(6678),p=t(11316),u=t(77161),g=t(15647),h=t(79877),m=t(94055);function x(e){return function(a){const t=new n.w0,x=(0,s.D)((0,h.Pq)({searchString:e.searchString,perPage:e.perPage,page:e.page,excludeUid:e.currentPanelId,sortDirection:e.sortDirection,typeFilter:e.panelFilter,folderFilter:e.folderFilter})).pipe((0,o.z)((e=>{let{perPage:a,elements:t,page:n,totalCount:s}=e;return(0,r.of)((0,m.zK)({libraryPanels:t,page:n,perPage:a,totalCount:s}))})),(0,c.K)((a=>(console.error(a),(0,r.of)((0,m.zK)(Object.assign({},m.p$,{page:e.page,perPage:e.perPage})))))),(0,d.x)((()=>t.unsubscribe())),(0,p.B)());t.add((0,i.T)((0,l.H)(50).pipe((0,u.h)((0,m.xU)()),(0,g.R)(x)),x).subscribe(a))}}function f(e,a){return async function(t){try{await(0,h.UO)(e),x(a)(t)}catch(e){console.error(e)}}}function b(e){return function(a){return a instanceof Function?a(e):e(a)}}},94055:(e,a,t)=>{t.d(a,{_p:()=>c,oO:()=>o,p$:()=>r,xU:()=>i,zK:()=>l});var n=t(84890),s=t(77212);const r={loadingState:s.Gu.Loading,libraryPanels:[],totalCount:0,perPage:40,page:1,numberOfPages:0,currentPanelId:void 0},i=(0,n.PH)("libraryPanels/view/initSearch"),l=(0,n.PH)("libraryPanels/view/searchCompleted"),o=(0,n.PH)("libraryPanels/view/changePage"),c=(e,a)=>{if(i.match(a))return Object.assign({},e,{loadingState:s.Gu.Loading});if(l.match(a)){const{libraryPanels:t,page:n,perPage:r,totalCount:i}=a.payload,l=Math.ceil(i/r);return Object.assign({},e,{libraryPanels:t,perPage:r,totalCount:i,loadingState:s.Gu.Done,numberOfPages:l,page:n>l?n-1:n})}return o.match(a)?Object.assign({},e,{page:a.payload.page}):e}},60105:(e,a,t)=>{t.d(a,{J:()=>s});var n=t(77813);function s(e){return{myTable:n.css`
      max-height: 204px;
      overflow-y: auto;
      margin-top: 11px;
      margin-bottom: 28px;
      border-radius: ${e.border.radius.sm};
      border: 1px solid ${e.colors.bg3};
      background: ${e.colors.bg1};
      color: ${e.colors.textSemiWeak};
      font-size: ${e.typography.size.md};
      width: 100%;

      thead {
        color: #538ade;
        font-size: ${e.typography.size.sm};
      }

      th,
      td {
        padding: 6px 13px;
        height: ${e.spacing.xl};
      }

      tbody > tr:nth-child(odd) {
        background: ${e.colors.bg2};
      }
    `,noteTextbox:n.css`
      margin-bottom: ${e.spacing.xl};
    `,textInfo:n.css`
      color: ${e.colors.textSemiWeak};
      font-size: ${e.typography.size.sm};
    `,dashboardSearch:n.css`
      margin-top: ${e.spacing.md};
    `,modal:n.css`
      width: 500px;
    `,modalText:n.css`
      font-size: ${e.typography.heading.h4};
      color: ${e.colors.link};
      margin-bottom: calc(${e.spacing.d} * 2);
      padding-top: ${e.spacing.d};
    `}}},973:(e,a,t)=>{t.d(a,{X:()=>u});var n=t(77813),s=(t(76687),t(37729)),r=t(9600),i=t(28441),l=t(27668),o=t(2338),c=t(9197),d=t(4471),p=t(52010);const u=e=>{let{isCurrent:a,title:t,plugin:r,onClick:c,onDelete:d,disabled:u,showBadge:m,description:x,children:f}=e;const b=(0,l.wW)(g),y=u||r.state===s.BV.deprecated,v=(0,n.cx)({[b.item]:!0,[b.itemDisabled]:y,[b.current]:a});return(0,p.jsxs)("div",{className:v,"aria-label":i.wl.components.PluginVisualization.item(r.name),onClick:y?void 0:c,title:a?"Click again to close this section":r.name,children:[(0,p.jsx)("img",{className:(0,n.cx)(b.img,{[b.disabled]:y}),src:r.info.logos.small,alt:""}),(0,p.jsxs)("div",{className:(0,n.cx)(b.itemContent,{[b.disabled]:y}),children:[(0,p.jsx)("div",{className:b.name,children:t}),x?(0,p.jsx)("span",{className:b.description,children:x}):null,f]}),m&&(0,p.jsx)("div",{className:(0,n.cx)(b.badge,{[b.disabled]:y}),children:(0,p.jsx)(h,{plugin:r})}),d&&(0,p.jsx)(o.h,{name:"trash-alt",onClick:e=>{e.stopPropagation(),d()},className:b.deleteButton,"aria-label":"Delete button on panel type card"})]})};u.displayName="PanelTypeCard";const g=e=>({item:n.css`
      position: relative;
      display: flex;
      flex-shrink: 0;
      cursor: pointer;
      background: ${e.colors.background.secondary};
      border-radius: ${e.shape.borderRadius()};
      box-shadow: ${e.shadows.z1};
      border: 1px solid ${e.colors.background.secondary};
      align-items: center;
      padding: 8px;
      width: 100%;
      position: relative;
      overflow: hidden;
      transition: ${e.transitions.create(["background"],{duration:e.transitions.duration.short})};

      &:hover {
        background: ${e.colors.emphasize(e.colors.background.secondary,.03)};
      }
    `,itemContent:n.css`
      overflow: hidden;
      position: relative;
      padding: ${e.spacing(0,1)};
    `,itemDisabled:n.css`
      cursor: default;

      &,
      &:hover {
        background: ${e.colors.action.disabledBackground};
      }
    `,current:n.css`
      label: currentVisualizationItem;
      border: 1px solid ${e.colors.primary.border};
      background: ${e.colors.action.selected};
    `,disabled:n.css`
      opacity: ${e.colors.action.disabledOpacity};
      filter: grayscale(1);
      cursor: default;
      pointer-events: none;
    `,name:n.css`
      text-overflow: ellipsis;
      overflow: hidden;
      font-size: ${e.typography.size.sm};
      font-weight: ${e.typography.fontWeightMedium};
      width: 100%;
    `,description:n.css`
      display: block;
      text-overflow: ellipsis;
      overflow: hidden;
      color: ${e.colors.text.secondary};
      font-size: ${e.typography.bodySmall.fontSize};
      font-weight: ${e.typography.fontWeightLight};
      width: 100%;
      max-height: 4.5em;
    `,img:n.css`
      max-height: 38px;
      width: 38px;
      display: flex;
      align-items: center;
    `,badge:n.css`
      background: ${e.colors.background.primary};
    `,deleteButton:n.css`
      cursor: pointer;
      margin-left: auto;
    `}),h=e=>{let{plugin:a}=e;return(0,r.x)(a.signature)?(0,p.jsx)(c.o,{status:a.signature}):(0,p.jsx)(d.u,{state:a.state})};h.displayName="PanelPluginBadge"},96029:(e,a,t)=>{t.d(a,{r:()=>l,x:()=>i});var n=t(37729),s=t(32397),r=t(72e3);function i(){const e=r.vc.panels;return Object.keys(e).filter((a=>!1===e[a].hideFromList)).map((a=>e[a])).sort(((e,a)=>e.sort-a.sort))}function l(e,a,t){if(!a.length)return e.filter((e=>e.state!==n.BV.deprecated||t.id===e.id));const r=(0,s.x6)(a).toLowerCase(),i=[],l=[],o="graph".startsWith(r);for(const a of e){if(a.state===n.BV.deprecated&&t.id!==a.id)continue;const e=a.name.toLowerCase().indexOf(r);0===e?i.push(a):e>0?l.push(a):o&&"timeseries"===a.id&&i.push(a)}return i.concat(l)}},4471:(e,a,t)=>{t.d(a,{u:()=>i});t(76687);var n=t(37729),s=t(94903),r=t(52010);const i=e=>{const a=function(e){switch(e){case n.BV.deprecated:return{text:"Deprecated",color:"red",tooltip:"This feature is deprecated and will be removed in a future release"};case n.BV.alpha:return{text:"Alpha",color:"blue",tooltip:"This feature is experimental and future updates might not be backward compatible"};case n.BV.beta:return{text:"Beta",color:"blue",tooltip:"This feature is close to complete but not fully tested"};default:return null}}(e.state);return a?(0,r.jsx)(s.C,{color:a.color,title:a.tooltip,text:a.text,icon:a.icon}):null}}}]);
//# sourceMappingURL=793.becb8349bd3efa23a590.js.map