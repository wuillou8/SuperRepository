# Google Analytics
Summary about google analytics.

### GA Premium VS Proletarium
costs: 150'000 GBP

"""We've lowered the barrier to enterprise analytics. Because the best numbers shouldn’t be just for those with the biggest pockets."""

#####additional features:
* additional reports.
* 1 billion hits per month
* Up to 3 million rows of data in unsampled reports
* 4-hour fresh data
* Guaranteed reliable data access, 24/7*
* Maximum safety and security for your data
* Data you own and fully control (not granted in proletarium)

documentation: http://www.jellyfish.co.uk/packages/jellyfish_website/themes/jellyfish/assets/JF_GoogleAnalytics_COMP_UK.pdf

### GA access to data

GA use case is probably mostly the support for the production of reports, etc.
One one hand, there are functionalities for querying the system about this or that. 

Aside of the automatised workflows, there is also for programmer the possibility to produce there own reports from the data. For instance you could query ids, a date range, with analytics.data.ga.get() and apply functions, filter, conditions, ...

More important for us is the possibility of specify on each pages which event have to be tracked, which has to be encoded with code snippets. These events are then stored into google analytics database and available, for instance through the functionalities presented in the last paragraph.

Code-wise, something like:
_trackEvent(category, action, opt_label, opt_value, opt_noninteraction)
with as important params:
category The general event category (e.g. "Videos"). 
action The action for the event (e.g. "Play"). 
opt_label An optional descriptor for the event.

An example of what people do with that stuff on the board in
https://www.youtube.com/watch?v=dERp9CYLAgg , around the 11th min.

Maybe worth to mention are the support for asynchronous tracking, which use case I am not sure.

### Documentation, a best of ...
* https://developers.google.com/analytics/devguides/collection/gajs/methods/
* Real time data: https://developers.google.com/analytics/devguides/reporting/realtime/v3/reference/data/realtime/get
* Core reporting: https://developers.google.com/analytics/devguides/reporting/core/v3/reference
* event tracking: https://developers.google.com/analytics/devguides/collection/gajs/eventTrackerGuide


### Actions and Events on GA
* scrolling: scrolling can be tracked, but I found only one examples concerning percentile of the page viewed.
* bouncing, average visit duration, clicks, video view, download: could be detected/measured

### Jair Summary & Questions:
* Prod. Intell. and Google Analytics
So, if I understand it correctly, the strategy would consist in putting some ga codes snippets into the 
pages we are creating, which would allow for getting the analytics/data we want back... through queries of ga...
 Analytics would be able to use ga functionalities to generate summaries, etc.

* Premium vs proletarium: 
could google analytics proletarium be a bottleneck in term of perfo. and is data privacy an issue we are concerned with?
      Is it an alternative to build ga inhouse, as the standard workflow will require development anyway.