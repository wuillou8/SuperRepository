<!DOCTYPE html>
<!-- saved from url=(0073)https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md -->
<html lang="en" class=" is-copy-enabled"><head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    <meta content="origin-when-crossorigin" name="referrer">
    
    <title>cn-metrics/README.md at master · thinktopic/cn-metrics</title>
    <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="https://github.com/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="https://github.com/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="https://github.com/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="https://github.com/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site"><meta content="summary" name="twitter:card"><meta content="thinktopic/cn-metrics" name="twitter:title"><meta content="cn-metrics - All your analytics are belong to us!" name="twitter:description"><meta content="https://avatars0.githubusercontent.com/u/7161962?v=3&amp;s=400" name="twitter:image:src">
      <meta content="GitHub" property="og:site_name"><meta content="object" property="og:type"><meta content="https://avatars0.githubusercontent.com/u/7161962?v=3&amp;s=400" property="og:image"><meta content="thinktopic/cn-metrics" property="og:title"><meta content="https://github.com/thinktopic/cn-metrics" property="og:url"><meta content="cn-metrics - All your analytics are belong to us!" property="og:description">
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/NDU1ODI5Njo4YzZkMTdhNjAzMThhMzA3NDI0YzgxYzNkYWU5YmQ5YzowMGMzMTFkOTc1ODlmN2FhNjNkNmVlMjA5ZTdiOGYyYzZiY2RiOWI5YzBkNWY2ZGY2YjRhNWEzYTczYWM2Nzll--f05c88f459603c3fdaaacdeb72b1a911c8a0328f">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    

        <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host"><meta content="collector-cdn.github.com" name="octolytics-script-host"><meta content="github" name="octolytics-app-id"><meta content="05940FF6:6D97:A7987A4:55C218B5" name="octolytics-dimension-request_id"><meta content="4558296" name="octolytics-actor-id"><meta content="wuillou8" name="octolytics-actor-login"><meta content="63eee55f12a3424d85b75e44bb98b071ecfddc65d2d9b0a04c47438e9855af54" name="octolytics-actor-hash">
    
    
    <meta class="js-ga-set" name="dimension1" content="Logged In">
      <meta class="js-ga-set" name="dimension4" content="Current repo nav">
    <meta name="is-dotcom" content="true">
        <meta name="hostname" content="github.com">
    <meta name="user-login" content="wuillou8">

      <link rel="icon" sizes="any" mask="" href="https://assets-cdn.github.com/pinned-octocat.svg">
      <meta name="theme-color" content="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <!-- </textarea> --><!-- '"` --><meta content="authenticity_token" name="csrf-param">
<meta content="ckLJ4wt8fwUpVg27RaUcDqAHC17zkPD1crGLifWfy7sWhxjoz/v3m1L/quULSCKHU5kYpxBDs56zLjb525T3KA==" name="csrf-token">
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github/index-a6099c44cba81e3cc01a25d5aad205f2dd86c56ad656d0ee72761a3db28828c5.css" media="all" rel="stylesheet">
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2/index-e7262cad01eef2691501230e7d70c976a8e97c8a96842f0f29a1f20f658a315d.css" media="all" rel="stylesheet">
    
    


    <meta http-equiv="x-pjax-version" content="7b3fb0c762b1609124fa6ce9de586ac0">

      
  <meta name="description" content="cn-metrics - All your analytics are belong to us!">
  <meta name="go-import" content="github.com/thinktopic/cn-metrics git https://github.com/thinktopic/cn-metrics.git">

  <meta content="7161962" name="octolytics-dimension-user_id"><meta content="thinktopic" name="octolytics-dimension-user_login"><meta content="36953205" name="octolytics-dimension-repository_id"><meta content="thinktopic/cn-metrics" name="octolytics-dimension-repository_nwo"><meta content="false" name="octolytics-dimension-repository_public"><meta content="false" name="octolytics-dimension-repository_is_fork"><meta content="36953205" name="octolytics-dimension-repository_network_root_id"><meta content="thinktopic/cn-metrics" name="octolytics-dimension-repository_network_root_nwo">
  <link href="https://github.com/thinktopic/cn-metrics/commits/master.atom?token=AEWN2BZrON3Fit6qZ04hHONVgFrptx5Cks6zz1lGwA%3D%3D" rel="alternate" title="Recent Commits to cn-metrics:master" type="application/atom+xml">

  <script type="text/javascript" async="" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/api.js"></script><meta name="selected-link" value="repo_source" data-pjax-transient="true"><meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event"><meta content="/private/private/blob/show" data-pjax-transient="true" name="analytics-location"></head>


  <body class="logged_in  env-production macintosh vis-private">
    <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/thinktopic/cn-metrics/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text" class="js-site-search-focus js-site-search-field is-clearable chromeless-input" data-hotkey="s" name="q" placeholder="Search" aria-label="Search this repository" data-global-scope-placeholder="Search GitHub" data-repo-scope-placeholder="Search" tabindex="1" autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="https://github.com/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="https://github.com/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content" data-channel="notification-changed:wuillou8" data-url="/notifications/header">
      <a href="https://github.com/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
          <span class="mail-status unread"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="https://github.com/new" aria-label="Create new…" data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="https://github.com/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="https://github.com/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="thinktopic/cn-metrics">This repository</span>
  </div>
    <a class="dropdown-item" href="https://github.com/thinktopic/cn-metrics/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-s js-menu-target" href="https://github.com/wuillou8" aria-label="View profile and more" data-ga-click="Header, show menu, icon:avatar">
      <img alt="@wuillou8" class="avatar" height="20" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/4558296" width="20">
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">wuillou8</strong>
        </div>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="https://github.com/wuillou8" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="https://github.com/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="https://github.com/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
        <a class="dropdown-item" href="https://help.github.com/" data-ga-click="Header, go to help, text:help">
          Help
        </a>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="https://github.com/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/logout" class="logout-form" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="RLPdjMqy5HKuXh1hQOYyKyB/9PP7El26YvHIurhM9DyQFHlEHZkXVHLj0G1XJWdTRIMybDYpstTUlDhDaoL92g=="></div>
          <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope="" itemtype="http://schema.org/WebPage">
    <div id="js-flash-container"><div id="pjax-flash">
  
</div></div>
    <div class="pagehead repohead instapaper_ignore readability-menu ">
      <div class="container">

        <div class="clearfix">
          
<ul class="pagehead-actions">

  <li>
      <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="wfk7VlsHWVsxwAtJKGXPOxVnnvAlzpzrzQWM0ZQVWnFcSozp8vC2r99R3CTRMgVWuXk3qir+o4qD+h1p81G2Dw=="></div>    <input id="repository_id" name="repository_id" type="hidden" value="36953205">

      <div class="select-menu js-menu-container js-select-menu">
        <a href="https://github.com/thinktopic/cn-metrics/subscription" class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true" data-ga-click="Repository, click Watch settings, action:files#disambiguate">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>
        <a class="social-count js-social-count" href="https://github.com/thinktopic/cn-metrics/watchers">
          15
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included">
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed">
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore">
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/unstar" class="js-toggler-form starred js-unstar-button" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="rA7KTC6pl/dpVk4dP+yqhY9OMxLZA7eNjEHbddnAkT+qbod9VFOAz5CTZRDDSuK6OaQdk7lwxLNz3vOmgPJK0g=="></div>
      <button class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar thinktopic/cn-metrics" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="https://github.com/thinktopic/cn-metrics/stargazers">
          0
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/star" class="js-toggler-form unstarred js-star-button" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="wmbwKDOXiR9pWOeFLnXOMkGKLuC6LpoNPQ5yjOXJxZENugnXufH33iTI7bGAtG0kDCMVcOuuFaz2Rxf+6EECvA=="></div>
      <button class="btn btn-sm btn-with-count js-toggler-target" aria-label="Star this repository" title="Star thinktopic/cn-metrics" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="https://github.com/thinktopic/cn-metrics/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#fork-destination-box" class="btn btn-sm btn-with-count" title="Fork your own copy of thinktopic/cn-metrics to your account" aria-label="Fork your own copy of thinktopic/cn-metrics to your account" rel="facebox" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="https://github.com/thinktopic/cn-metrics/network" class="social-count">1</a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src="" class="js-fork-select-fragment fork-select-fragment" data-url="/thinktopic/cn-metrics/fork?fragment=1">
              <img alt="Loading" height="64" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-128.gif" width="64">
            </include-fragment>
          </div>
        </li>

</ul>

          <h1 itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title private ">
            <span class="mega-octicon octicon-lock"></span>
            <span class="author"><a href="https://github.com/thinktopic" class="url fn" itemprop="url" rel="author"><span itemprop="title">thinktopic</span></a></span><!--
         --><span class="path-divider">/</span><!--
         --><strong><a href="https://github.com/thinktopic/cn-metrics" data-pjax="#js-repo-pjax-container">cn-metrics</a></strong>
              <span class="repo-private-label">private</span>

            <span class="page-context-loader">
              <img alt="" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
            </span>

          </h1>
        </div>

      </div>
    </div>

      <div class="container">
        <div class="repository-with-sidebar repo-container new-discussion-timeline">
          <div class="repository-sidebar clearfix">
              

<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders" role="navigation" data-pjax="#js-repo-pjax-container" data-issue-count-url="/thinktopic/cn-metrics/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="https://github.com/thinktopic/cn-metrics" aria-label="Code" aria-selected="true" class="js-selected-navigation-item sunken-menu-item selected" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /thinktopic/cn-metrics">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="https://github.com/thinktopic/cn-metrics/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /thinktopic/cn-metrics/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="counter">0</span>

          <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="https://github.com/thinktopic/cn-metrics/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /thinktopic/cn-metrics/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="counter">0</span>

          <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="https://github.com/thinktopic/cn-metrics/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /thinktopic/cn-metrics/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="https://github.com/thinktopic/cn-metrics/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /thinktopic/cn-metrics/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="https://github.com/thinktopic/cn-metrics/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /thinktopic/cn-metrics/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/octocat-spinner-32.gif" width="16">
</a>    </li>
  </ul>


</nav>

                <div class="only-with-full-nav">
                    
<div class="js-clone-url clone-url " data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target" value="https://github.com/thinktopic/cn-metrics.git" readonly="readonly" aria-label="HTTPS clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url open" data-protocol-type="ssh">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target" value="git@github.com:thinktopic/cn-metrics.git" readonly="readonly" aria-label="SSH clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url " data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target" value="https://github.com/thinktopic/cn-metrics" readonly="readonly" aria-label="Subversion checkout URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



  <div class="clone-options">You can clone with
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/users/set_protocol?protocol_selector=http&protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="B+tejzofkR7vefqHCYu+wYxwASnwPfIkDn8SlF/UD/ddnV7axGzfNK+pUdE9YCLv1IJCs3rplRo2og+5liHgeg=="></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form>, <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/users/set_protocol?protocol_selector=ssh&protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="Wc15u9fXokKl1Ru6A2/u/ZCHLj8uhRD5dBYt/qtzlzSz1ksGfDMhEpQBDeN8O4fV4l1Yq7jpO5qxJFvFYivUAg=="></div><button class="btn-link js-clone-selector" data-protocol="ssh" type="submit">SSH</button></form>, or <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/users/set_protocol?protocol_selector=subversion&protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="TVOXxdj0FCRnE1G4IfgKdZ9rhxOTSuvlJhakPhIv9HWwypsy+XZQvxRhdbC1F44Siic3R1b99Ix3BwZ/95hbpw=="></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
    <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
      <span class="octicon octicon-question"></span>
    </a>
  </div>
    <a href="https://mac.github.com/" class="btn btn-sm sidebar-button" title="Save thinktopic/cn-metrics to your computer and use it in GitHub Desktop." aria-label="Save thinktopic/cn-metrics to your computer and use it in GitHub Desktop.">
      <span class="octicon octicon-device-desktop"></span>
      Clone in Desktop
    </a>

                  <a href="https://github.com/thinktopic/cn-metrics/archive/master.zip" class="btn btn-sm sidebar-button" aria-label="Download the contents of thinktopic/cn-metrics as a zip file" title="Download the contents of thinktopic/cn-metrics as a zip file" rel="nofollow">
                    <span class="octicon octicon-cloud-download"></span>
                    Download ZIP
                  </a>
                </div>
          </div>
          <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container="">  

<a href="https://github.com/thinktopic/cn-metrics/blob/9667025e1b36cdb839755313f04a008e0992f7a8/metrics-ui/README.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:d9a9f89a51ae78d0d25c3c3f8c674b2a -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w" data-ref="master" title="master" role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax="" aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected" href="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/cn-metrics_README.md at master · thinktopic_cn-metrics.html" data-name="master" data-skip-pjax="true" rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="T8HQezsY5q2Y6O9x7IqX1D1nObcxFBL7pFFcl/379f0GzXfFibqAvzvHMqMhJ5s7YFCU+FM68XJ1S1PV4BrfYg=="></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="metrics-ui/README.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="btn-group right">
      <a href="https://github.com/thinktopic/cn-metrics/find/master" class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-nw" data-pjax="" data-hotkey="t" aria-label="Quickly jump between files">
        <span class="octicon octicon-list-unordered"></span>
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </div>

    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="https://github.com/thinktopic/cn-metrics" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">cn-metrics</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="https://github.com/thinktopic/cn-metrics/tree/master/metrics-ui" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">metrics-ui</span></a></span><span class="separator">/</span><strong class="final-path">README.md</strong>
    </div>
  </div>



  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@wuillou8" class="avatar" height="24" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/4558296(1)" width="24">
        <span class="author"><a href="https://github.com/wuillou8" rel="contributor">wuillou8</a></span>
        <time datetime="2015-08-05T11:02:59Z" is="relative-time" title="Aug 5, 2015, 12:02 PM GMT+1">3 hours ago</time>
        <div class="commit-title">
            <a href="https://github.com/thinktopic/cn-metrics/commit/9667025e1b36cdb839755313f04a008e0992f7a8" class="message" data-pjax="true" title="updated readme">updated readme</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@wuillou8" height="24" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/4558296(1)" width="24">
            <a href="https://github.com/wuillou8">wuillou8</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="https://github.com/thinktopic/cn-metrics/raw/master/metrics-ui/README.md" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="https://github.com/thinktopic/cn-metrics/blame/master/metrics-ui/README.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="https://github.com/thinktopic/cn-metrics/commits/master/metrics-ui/README.md" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw" href="https://mac.github.com/" aria-label="Open this file in GitHub for Mac" data-ga-click="Repository, open with desktop, type:mac">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/edit/master/metrics-ui/README.md" class="inline-form" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="QLyTCRHSlzpS23hje19GDs++WdyOiHInUxDcM8M0ZiR0aT1j66fsz6vSSUieLsy26Mq0+wVj+26/zLnCrwCFFw=="></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Edit this file" data-hotkey="e" data-disable-with="">
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="https://github.com/thinktopic/cn-metrics/delete/master/metrics-ui/README.md" class="inline-form" data-form-nonce="6cd850c9488808d3e5aa75bd66f73a30e6ac825a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"><input name="authenticity_token" type="hidden" value="FJRprxxazYx3Dg/choHC11jzHJKXD0G08WJn+4C82bLyDyKcMtj9MqD6ZMfPOHom41R8rpgAnaOVJ6bzUv3rMg=="></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Delete this file" data-disable-with="">
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        47 lines (36 sloc)
        <span class="file-info-divider"></span>
      1.613 kB
    </div>
  </div>
  
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h1><a id="user-content-tagging-library" class="anchor" href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#tagging-library" aria-hidden="true"><span class="octicon octicon-link"></span></a>Tagging Library</h1>

<p>This is a tagging library for CN website. The events are stored into the cassandra database.</p>

<h3><a id="user-content-tags-function" class="anchor" href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#tags-function" aria-hidden="true"><span class="octicon octicon-link"></span></a>Tags function</h3>

<p>The tag function is defined on resources/public/style_event.js
and has the following fields (expecting hashmaps):  </p>

<pre><code>function send_event(userdata, category, action, eventdata, pagedata);
</code></pre>

<p>whereas:    </p>

<ul>
<li>userdata: data about the user (userId, country, ethnic origin, sexual orientation, mother's name, favourite recipe, political stance, ...)</li>
<li>category: for now, 'browse' or 'transaction',</li>
<li>action: for instance view, click, menu-navigation (in browse) or  place in cart, buy, payment confirmation (transaction),</li>
<li>eventdata:    for a 'browser' category event, a hashmap with for instance a button details. For a 'transaction' event, for instance product and transaction details (id, brand, price, costs).</li>
<li>pagedata: data about the page viewed, ideally a list of parameters encoding the particular webpage.</li>
</ul>

<h3><a id="user-content-examples" class="anchor" href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#examples" aria-hidden="true"><span class="octicon octicon-link"></span></a>Examples</h3>

<p>For now, find examples on resources/public/test.html</p>

<p>As a summary:<br>
window.user = {id: "user1234",
               country: "france"}<br>
window.view = {id: "view"}<br>
window.pagedata = {
    id: "a std page",
    param1: "param1 ..."
    }<br>
window.click = {id: "click"}<br>
window.menu = {id: "menu"}<br>
window.prod1 = {
    id: "P1",
    name: "T-Shirt",
    category: "Clothing",
    brand: "Google",
    variant: "black",
    price: "29.20",
    costs: "18.75"
    }</p>

<p>calls:</p>

<pre><code>&lt;button onClick="send_event(window.user, 'browse', 'view', window.view, window.pagedata)"&gt;
&lt;send_event(window.user, 'transaction', 'purchase', window.item, window.pagedata)    
</code></pre>
</article>
  </div>

</div>

<a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line…" aria-label="Jump to line" autofocus="">
    <button type="submit" class="btn">Go</button>
</form></div>




</div>
        </div>
        <div class="modal-backdrop"></div>
      </div>
  </div>


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com/" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com/" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com/" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://help.github.com/" data-ga-click="Footer, go to help, text:help">Help</a></li>

    </ul>

    <a href="https://github.com/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>© 2015 <span title="0.06772s from github-fe116-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" aria-label=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w" aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="https://github.com/thinktopic/cn-metrics/blob/master/metrics-ui/README.md#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/frameworks-60fa9d481f93b9638a55282fc13cd1e893f5da608855190c2259c5b35883105c.js"></script>
      <script async="async" crossorigin="anonymous" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/index-4864e54542a25a0f1dc884a414b7fee9b624d1717ce4a61500d1e23907a794ac.js"></script>
      
      
  


    <div class="facebox" id="facebox" style="display:none;">       <div class="facebox-popup">         <div class="facebox-content">         </div>         <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">           <span class="octicon octicon-remove-close"></span>         </button>       </div>     </div><div id="jsConsole" style="bottom:5px;right:0px;position:fixed; z-index:10000000 !important;background-color:white"><div style="display: none;" id="icon" rows="1" cols="1"><img style="display: none;" id="DTM" title="DTM" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/price_tag-16.png">&nbsp;&nbsp;&nbsp;<img style="display: none;" id="Analytics" title="Analytics" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/chart_bar.png">&nbsp;&nbsp;&nbsp;<img style="display: none;" id="Target" title="Target" src="./cn-metrics_README.md at master · thinktopic_cn-metrics_files/Human_resource_strategy-09-16.png"></div><textarea id="tv" rows="1" onkeypress="if (event.keyCode == 13) { return false;  }" style="font-size: 10pt;overflow:hidden;resize: none;display:none;clear:left;width: 80px;height: 19px; font-size: 15px;        border: 1px solid #cccccc;        padding: 2px;        font-family: Tahoma, sans-serif;                background-position: bottom right;        background-repeat: no-repeat;" onfocusout="var data = {};data[&#39;Omni&#39;] = { cd_debug:  document.getElementById(&#39;bodyCode&#39;).style.display ,flag: this.value, cd_counter:document.getElementById(&#39;jsnline&#39;).value};localStorage[&#39;data&#39;] = JSON.stringify(data);document.getElementById(&#39;tv&#39;).style.display=&#39;inline&#39;;eval(document.getElementById(&#39;jsCode&#39;).value);"></textarea><textarea id="tvarCode" onkeypress="if (event.keyCode == 13) { return false; }" rows="1" style="font-size: 10pt;overflow:hidden;	resize: none;display:none;clear:left;width: 220px;height: 19px;font-size: 15px;        border: 1px solid #cccccc;        padding: 2px;        font-family: Tahoma, sans-serif;                background-position:  right;        background-repeat: no-repeat;"></textarea><input id="jsnline" type="button" value="1" style="display:inline;float:right;font-family: Arial, Helvetica, sans-serif;	font-size: 11px;	color: #ffffff;	padding: 4px ;	background: -moz-linear-gradient(top,#00c71e 0%,#039419);background: -webkit-gradient(	linear, left top, left bottom, 		from(#00c71e),		to(#039419));	border-radius: 0px;	-moz-border-radius: 0px;	-webkit-border-radius: 0px;	border: 1px solid #327d00;	-moz-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	-webkit-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	text-shadow:		0px -1px 0px rgba(000,000,000,0.4),		0px 1px 0px rgba(255,255,255,0.3);" onclick="window.open(&#39;&#39;,&#39;dp_debugger&#39;,&#39;width=600,height=600,top=50,left=2000,location=0,menubar=0,status=1,toolbar=0,resizable=1,scrollbars=1&#39;).document.write(&#39;&lt;script id=dbg src=https://www.adobetag.com/d1/digitalpulsedebugger/live/DPD.js&gt;&lt;/script&gt;&#39;)"><input id="jsShowSourceButton" type="button" value="Tag Found" style="display:none;float:right;font-family: Arial, Helvetica, sans-serif;	font-size: 11px;	color: #ffffff;	padding: 4px ;	background: -moz-linear-gradient(top,#00c71e 0%,#039419);background: -webkit-gradient(	linear, left top, left bottom, 		from(#00c71e),		to(#039419));	border-radius: 0px;	-moz-border-radius: 0px;	-webkit-border-radius: 0px;	border: 1px solid #327d00;	-moz-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	-webkit-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	text-shadow:		0px -1px 0px rgba(000,000,000,0.4),		0px 1px 0px rgba(255,255,255,0.3);" onclick="document.getElementById(&#39;bodyCode&#39;).style.display=&#39;inline&#39;;eval(document.getElementById(&#39;jsCode&#39;).value);document.getElementById(&#39;scode&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsShowSourceButton&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugShowSourceButton&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugHideAllButton&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;tv&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;tvarCode&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsnline&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsDebugHideSourceButton&#39;).style.display=&#39;inline&#39;;"><input id="jsDebugShowSourceButton" type="button" value="Tag Found" style="display:none;float:right;font-family: Arial, Helvetica, sans-serif;	font-size: 11px;	color: #ffffff;	padding: 4px ;	background: -moz-linear-gradient(top,#00c71e 0%,#039419);background: -webkit-gradient(	linear, left top, left bottom, 		from(#00c71e),		to(#039419));	border-radius: 0px;	-moz-border-radius: 0px;	-webkit-border-radius: 0px;	border: 1px solid #327d00;	-moz-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	-webkit-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	text-shadow:		0px -1px 0px rgba(000,000,000,0.4),		0px 1px 0px rgba(255,255,255,0.3);" onclick="var data = {};data[&#39;Omni&#39;] = { cd_debug: &#39;inline&#39;, flag:  document.getElementById(&#39;tv&#39;).value, cd_counter:document.getElementById(&#39;jsnline&#39;).value  };localStorage[&#39;data&#39;] = JSON.stringify(data);eval(document.getElementById(&#39;jsCode&#39;).value);document.getElementById(&#39;jsDebugHideAllButton&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;bodyCode&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;scode&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsnline&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsDebugHideSourceButton&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;tv&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;tvarCode&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;jsDebugShowSourceButton&#39;).style.display=&#39;none&#39;;"><input id="jsDebugHideSourceButton" type="button" value="Hide Details" style="display:none;float:right;font-family: Arial, Helvetica, sans-serif;	font-size: 11px;	color: #ffffff;	padding: 4px ;	background: -moz-linear-gradient(top,#00c71e 0%,#039419);background: -webkit-gradient(	linear, left top, left bottom, 		from(#00c71e),		to(#039419));	border-radius: 0px;	-moz-border-radius: 0px;	-webkit-border-radius: 0px;	border: 1px solid #327d00;	-moz-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	-webkit-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	text-shadow:		0px -1px 0px rgba(000,000,000,0.4),		0px 1px 0px rgba(255,255,255,0.3);" onclick="var data = {};data[&#39;Omni&#39;] = { cd_debug: &#39;none&#39;, flag:  document.getElementById(&#39;tv&#39;).value, cd_counter:document.getElementById(&#39;jsnline&#39;).value  };localStorage[&#39;data&#39;] = JSON.stringify(data);document.getElementById(&#39;bodyCode&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;scode&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugHideAllButton&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsnline&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugHideSourceButton&#39;).style.display=&#39;none&#39;;if(document.getElementById(&#39;bodyCode&#39;).value==&#39;&#39;)document.getElementById(&#39;jsDebugShowSourceButton&#39;).value = &#39;No Tag&#39;;if(document.getElementById(&#39;bodyCode&#39;).value==&#39;&#39;)document.getElementById(&#39;jsShowSourceButton&#39;).value = &#39;No Tag&#39;;document.getElementById(&#39;jsShowSourceButton&#39;).style.display=&#39;inline&#39;;"><input id="jsDebugHideAllButton" type="button" value="Hide All" style="display:none;float:right;font-family: Arial, Helvetica, sans-serif;	font-size: 11px;	color: #ffffff;	padding: 4px ;	background: -moz-linear-gradient(top,#00c71e 0%,#039419);background: -webkit-gradient(	linear, left top, left bottom, 		from(#00c71e),		to(#039419));	border-radius: 0px;	-moz-border-radius: 0px;	-webkit-border-radius: 0px;	border: 1px solid #327d00;	-moz-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	-webkit-box-shadow:		0px 1px 3px rgba(003,003,003,0.5),		inset 0px 0px 2px rgba(255,255,255,0.7);	text-shadow:		0px -1px 0px rgba(000,000,000,0.4),		0px 1px 0px rgba(255,255,255,0.3);" onclick="var data = {};data[&#39;Omni&#39;] = { cd_debug: &#39;hidden&#39;, flag:  document.getElementById(&#39;tv&#39;).value, cd_counter:document.getElementById(&#39;jsnline&#39;).value  };localStorage[&#39;data&#39;] = JSON.stringify(data);document.getElementById(&#39;bodyCode&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;scode&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsnline&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugHideSourceButton&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsDebugHideAllButton&#39;).style.display=&#39;none&#39;;document.getElementById(&#39;jsShowSourceButton&#39;).style.display=&#39;inline&#39;;document.getElementById(&#39;tv&#39;).style.display=&#39;none&#39;;if(document.getElementById(&#39;bodyCode&#39;).value==&#39;&#39;)document.getElementById(&#39;jsDebugShowSourceButton&#39;).value = &#39;No Tag&#39;;if(document.getElementById(&#39;bodyCode&#39;).value==&#39;&#39;)document.getElementById(&#39;jsShowSourceButton&#39;).value = &#39;No Tag&#39;;document.getElementById(&#39;tvarCode&#39;).style.display=&#39;none&#39;;"><div id="scode" rows="5" cols="3" style="float:right;clear:right;width: 500px; height: 60px;        border: 1px solid #cccccc;        padding: 5px;        font-family: Tahoma, sans-serif; font-size: 8pt;             background-color: white;  background-position: bottom right;        background-repeat: no-repeat;"></div><textarea id="bodyCode" rows="40" cols="70" style="display:none;float:right;clear:right;width: 500px; height: 430px;        border: 1px solid #cccccc;        padding: 5px;        font-family: Tahoma, sans-serif;                background-position: bottom right;        background-repeat: no-repeat;"></textarea><textarea id="jsCode" rows="5" cols="60" style="display:none;float:right;clear:right;">var j=document.styleSheets,i=document.images,r='',ff='',nono='',separator="---------------- IMAGE REQUEST ----------------";var nline=0;var nodes = document.getElementsByTagName('script');for(var i=0;i&lt;nodes.length;i++){var node = nodes[i];nono=node.src;if(nono){if((nono.indexOf('satellite')&gt;-1) || (nono.indexOf('adobetag')&gt;-1) || (nono.indexOf('s_code')&gt;-1) || (nono.indexOf('mboxPC')&gt;-1)){document.getElementById("icon").style.display="inline";if(nono.indexOf('satellite')&gt;-1 || nono.indexOf('adobetag')&gt;-1){document.getElementById("DTM").style.display="inline";}if(nono.indexOf('mboxPC')&gt;-1){document.getElementById("Target").style.display="inline";}ff+="&lt;a target='_blank' href='"+nono+"'&gt;"+nono+"&lt;/a&gt;"+"&lt;BR&gt;";}}} document.getElementById('scode').innerHTML=ff;for(var x=0;x&lt;j.length;x++)if(j[x].imports)for(var y=0;y&lt;j[x].imports.length;y++)if(j[x].imports[y].href.toLowerCase().indexOf('/b/ss/')&gt;=0)r+=j[x].imports[y].href+"*************\n\n";for(var x=0;x&lt;i.length;x++)if(i[x].src.toLowerCase().indexOf('/b/ss/')&gt;=0)r+=i[x].src+"*************\n\n";for(w_m in window)if(w_m.substring(0,4)=='s_i_'&amp;&amp;window[w_m].src)if(window[w_m].src.indexOf('/b/ss/')&gt;=0){separator="---------------- IMAGE REQUEST ----------------";if(window[w_m].src.indexOf('lnk_o')&gt;=0){separator="----------------&gt;&gt;ONCLICK REQUEST&lt;&lt;----------------"}if(window[w_m].src.indexOf('pev3=video')&gt;=0){separator="----------------&gt;&gt;VIDEO REQUEST&lt;&lt;----------------"}if(window[w_m].src.indexOf('lnk_e')&gt;=0){separator="----------------&lt;EXIT LINK&gt;---------------- "};document.getElementById("Analytics").style.display="inline";nline=nline+1,r+=separator+'#'+nline+'\n'+window[w_m].src.substring(0,window[w_m].src.indexOf("&amp;s=",0))+"\n\n";} var tvar = document.getElementById('tv').value ; tvar = tvar + "=" ; r=unescape(r).substring(0,100000).replace(/&amp;ns=/g,'&amp;namespace=').replace(/&amp;ch=/g,'&amp;ch=').replace(/&amp;g=/g,'&amp;url=').replace(/&amp;r=/g,'referrer=').replace(/&amp;ndh=/g,'&amp;ndh=').replace(/&amp;pageName=/g,'&amp;pagename=').replace(/&amp;h/g,'&amp;hier').replace(/&amp;v/g,'&amp;evar').replace(/&amp;events=/g,'&amp;events=').replace(/&amp;products=/g,'&amp;products=').replace(/&amp;c/g,'&amp;prop').replace(/&amp;evar0/g,'&amp;campaign').replace(/&amp;propc=/g,'&amp;cc=').replace(/&amp;prope=/g,'&amp;ce=').replace(/&amp;proph=/g,'&amp;channel=').replace(/&amp;evarmt=/g,'&amp;vmt=').replace(/&amp;evarmf=/g,'&amp; vmf=').replace(/&amp;propl=/g,'&amp;cl=').replace(/&amp;/g,'\n');document.getElementById('bodyCode').value=localStorage['mbox'] + r ;document.getElementById('jsnline').value=nline;if(nline&gt;1){document.getElementById('jsnline').style.background='black';setTimeout("document.getElementById('jsnline').style.background='red';",100);document.getElementById('jsDebugShowSourceButton').style.background='red';document.getElementById('jsDebugShowSourceButton').value='Tags Found';}if(unescape(r).indexOf(tvar,0)&gt;0){document.getElementById('tvarCode').value=r.substring(r.indexOf(tvar,0),1000).replace(tvar,"");}if(typeof s === 'object' &amp;&amp; nline &amp;&amp; nline == 1){(function() {var oldVersion = s.t;s.t = function() {var result = oldVersion.apply(this, arguments); eval(document.getElementById('jsCode').value); bodyCode.scrollTop = bodyCode.scrollHeight * (bodyCode.value.substring(0,bodyCode.value.lastIndexOf('-----')).split('\n').length/bodyCode.value.split('\n').length) - 50;return result; };})();} if(nline&gt;1){ document.getElementById('jsDebugShowSourceButton').style.background='red'; document.getElementById('jsShowSourceButton').style.background='red';}</textarea></div></body></html>