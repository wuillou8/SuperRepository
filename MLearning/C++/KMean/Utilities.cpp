/////////////////////////////////////////////////////////////////////
//      Utilities Functions                                        //
/////////////////////////////////////////////////////////////////////

double randf(double m)
{	return m * rand() / (RAND_MAX - 1.);
}

inline double dist2(KMean::point a, KMean::point b)
{
	double x = a->x - b->x, y = a->y - b->y;
	return x*x + y*y;
}

inline int
nearest(KMean::point pt, KMean::point cent, int n_cluster, double *d2)
{
	int i, min_i;
	KMean::point c;
	double d, min_d;
	for (c = cent, i = 0; i < n_cluster; i++, c++)
	{ 
		min_d = HUGE_VAL;
		min_i = pt->group;
		for (c = cent, i = 0; i < n_cluster; i++, c++) {
			if (min_d > (d = dist2(c, pt))) {
				min_d = d; min_i = i;
			}
		}
	}

	if (d2) *d2 = min_d;
	{ return min_i; }
}

void kpp(KMean::point pts, int len, KMean::point cent, int n_cent)
{
	int i, j;
	int n_cluster;//for (c = cent, i = 0; i < n_cluster; i++, c++)
	double sum, *d = (double*)new double[len];
 
	KMean::point p, c;

	cent[0] = pts[ rand() % len ];
	for (n_cluster = 1; n_cluster < n_cent; n_cluster++) 
	{
		for (j = 0, p = pts; j < len; j++, p++)	
		{ sum = 0; }

		for (j = 0, p = pts; j < len; j++, p++)
		{
			nearest(p, cent, n_cluster, d + j);
			sum += d[j];
		}
		sum = randf(sum);
		for (j = 0, p = pts; j < len; j++, p++) 
		{
			if ((sum -= d[j]) > 0) continue;
			cent[n_cluster] = pts[j];
			break;
		}
	}
	for (j = 0, p = pts; j < len; j++, p++)
	{ p->group = nearest(p, cent, n_cluster, 0); }
	delete[] d;
}

void print_eps(KMean::point pts, int len, KMean::point cent, int n_cluster)
{
#	define W 400
#	define H 400
	int i, j;
	KMean::point p, c;
	double min_x, max_x, min_y, max_y, scale, cx, cy;
	double *colors = (double*)new double[n_cluster * 3];
 
	for (c = cent, i = 0; i < n_cluster; i++, c++)
	{
		colors[3*i + 0] = (3 * (i + 1) % 11)/11.;
		colors[3*i + 1] = (7 * i % 11)/11.;
		colors[3*i + 2] = (9 * i % 11)/11.;
	}
 
	max_x = max_y = -(min_x = min_y = HUGE_VAL);
	for (j = 0, p = pts; j < len; j++, p++) 
	{
		if (max_x < p->x) max_x = p->x;
		if (min_x > p->x) min_x = p->x;
		if (max_y < p->y) max_y = p->y;
		if (min_y > p->y) min_y = p->y;
	}
	scale = W / (max_x - min_x);
	if (scale > H / (max_y - min_y)) scale = H / (max_y - min_y);
	cx = (max_x + min_x) / 2;
	cy = (max_y + min_y) / 2;
 
	printf("%%!PS-Adobe-3.0\n%%%%BoundingBox: -5 -5 %d %d\n", W + 10, H + 10);
	printf( "/l {rlineto} def /m {rmoveto} def\n"
		"/c { .25 sub exch .25 sub exch .5 0 360 arc fill } def\n"
		"/s { moveto -2 0 m 2 2 l 2 -2 l -2 -2 l closepath "
		"	gsave 1 setgray fill grestore gsave 3 setlinewidth"
		" 1 setgray stroke grestore 0 setgray stroke }def\n"
	);
	for (c = cent, i = 0; i < n_cluster; i++, c++)
	{
		printf("%g %g %g setrgbcolor\n",
			colors[3*i], colors[3*i + 1], colors[3*i + 2]);
		for (j = 0, p = pts; j < len; j++, p++)
		{
			if (p->group != i) continue;
			printf("%.3f %.3f c\n",
				(p->x - cx) * scale + W / 2,
				(p->y - cy) * scale + H / 2);
		}
		printf("\n0 setgray %g %g s\n",
			(c->x - cx) * scale + W / 2,
			(c->y - cy) * scale + H / 2);
	}
	printf("\n%%%%EOF");
	delete[] colors;
}