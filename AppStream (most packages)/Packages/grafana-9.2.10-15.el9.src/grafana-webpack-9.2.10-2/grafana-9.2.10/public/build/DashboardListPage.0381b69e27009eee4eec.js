"use strict";(self.webpackChunkgrafana=self.webpackChunkgrafana||[]).push([[4074],{49595:(e,a,s)=>{s.r(a),s.d(a,{DashboardListPage:()=>A,default:()=>T});var r=s(77813),n=s(76687),o=s(68021),t=s(83272),l=s(49622),d=s(28781),i=s(75477),c=s(92114);var h,u,p=s(27322),m=s(67273),g=s(27668),v=s(9120),f=s(69369),b=s(352),x=s(14970),w=s(74841),j=s(92691),y=s(58794),N=s(18173),C=s(21438),I=s(55312),D=s(39756),k=s(52010);const F=e=>{let{folderId:a,canCreateFolders:s=!1,canCreateDashboards:r=!1}=e;const n=e=>{let s=`dashboard/${e}`;return a&&(s+=`?folderId=${a}`),s};return(0,k.jsx)("div",{children:(0,k.jsx)(C.L,{overlay:()=>(0,k.jsxs)(N.v,{children:[r&&(0,k.jsx)(N.v.Item,{url:n("new"),label:"New Dashboard"}),!a&&s&&(h||(h=(0,k.jsx)(N.v.Item,{url:"dashboards/folder/new",label:"New Folder"}))),r&&(0,k.jsx)(N.v.Item,{url:n("import"),label:"Import"})]}),placement:"bottom-start",children:u||(u=(0,k.jsxs)(I.zx,{variant:"primary",children:["New",(0,k.jsx)(D.J,{name:"angle-down"})]}))})})};const $=n.memo((e=>{var a;let{folder:s}=e;const n=(0,g.wW)(W),{query:o,onQueryChange:t}=(0,j.A)({}),{onKeyDown:l,keyboardEvents:d}=(0,w.A)(),i=null==s?void 0:s.id,c=null==s?void 0:s.canSave,{isEditor:h}=f.Vt,u=s?c:f.Vt.hasEditPermissionInFolders,N=f.Vt.hasAccess(b.bW.FoldersCreate,h),C=u||!!c,I=null!=s&&s.id?f.Vt.hasAccessInMetadata(b.bW.DashboardsCreate,s,C):f.Vt.hasAccess(b.bW.DashboardsCreate,C),D=void 0===s&&N||I;let[$,P]=(0,p.Z)(x.to,!0);m.v.featureToggles.panelTitleSearch||($=!1);return(0,k.jsxs)(k.Fragment,{children:[(0,k.jsxs)("div",{className:(0,r.cx)(n.actionBar,"page-action-bar"),children:[(0,k.jsx)("div",{className:(0,r.cx)(n.inputWrapper,"gf-form gf-form--grow m-r-2"),children:(0,k.jsx)(v.I,{value:null!==(a=o.query)&&void 0!==a?a:"",onChange:e=>{t(e.currentTarget.value)},onKeyDown:l,autoFocus:!0,spellCheck:!1,placeholder:$?"Search for dashboards and panels":"Search for dashboards",className:n.searchInput,suffix:null})}),D&&(0,k.jsx)(F,{folderId:i,canCreateFolders:N,canCreateDashboards:I})]}),(0,k.jsx)(y.Z,{showManage:h||u||c,folderDTO:s,hidePseudoFolders:!0,includePanels:$,setIncludePanels:P,keyboardEvents:d})]})}));$.displayName="ManageDashboardsNew";const P=$,W=e=>({actionBar:r.css`
    ${e.breakpoints.down("sm")} {
      flex-wrap: wrap;
    }
  `,inputWrapper:r.css`
    ${e.breakpoints.down("sm")} {
      margin-right: 0 !important;
    }
  `,searchInput:r.css`
    margin-bottom: 6px;
    min-height: ${e.spacing(4)};
  `,unsupported:r.css`
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    font-size: 18px;
  `,noResults:r.css`
    padding: ${e.v1.spacing.md};
    background: ${e.v1.colors.bg2};
    font-style: italic;
    margin-top: ${e.v1.spacing.md};
  `}),A=(0,n.memo)((e=>{let{match:a,location:s}=e;const{loading:n,value:h}=(0,o.Z)((()=>{const e=a.params.uid,r=s.pathname;return e&&r.startsWith("/dashboards")?(e=>i.ae.getFolderByUid(e,{withAccessControl:!0}).then((e=>{const a=(0,c.B)(e);return a.children[0].active=!0,{folder:e,folderNav:a}})))(e).then((e=>{let{folder:a,folderNav:r}=e;const n=t.u.stripBaseFromUrl(a.url);return n!==s.pathname&&l.E1.replace(n),{folder:a,pageNav:r}})):Promise.resolve({})}),[a.params.uid]);return(0,k.jsx)(d.T,{navId:"dashboards/browse",pageNav:null==h?void 0:h.pageNav,children:(0,k.jsx)(d.T.Contents,{isLoading:n,className:r.css`
          display: flex;
          flex-direction: column;
          overflow: hidden;
        `,children:(0,k.jsx)(P,{folder:null==h?void 0:h.folder})})})}));A.displayName="DashboardListPage";const T=A}}]);
//# sourceMappingURL=DashboardListPage.0381b69e27009eee4eec.js.map