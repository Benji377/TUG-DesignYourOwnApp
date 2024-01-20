 <%!
     from pdoc.html_helpers import minify_css
 %>
 <%def name="homelink()" filter="minify_css">
     .homelink {
         display: block;
         font-size: 1em;
         font-weight: bold;
         padding-bottom: .5em;
         padding-top: .5em;
         border-bottom: 1px solid silver;
     }
     .homelink:hover {
         color: inherit;
     }
     .homelink img {
         width:100%;
         margin: auto;
         margin-bottom: .3em;
     }
 </%def>

 <style>${homelink()}</style>