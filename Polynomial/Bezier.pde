void setup(){
  size(800,800);
  background(255);
}

void draw(){
  
  int[] p0=new int[2];
  int[] p1=new int[2];
  int[] p2=new int[2];
  p0[0]=100;
  p0[1]=200;
  p1[0]=1;
  p1[1]=750;
  p2[0]=800;
  p2[1]=700;
  
  strokeWeight(8);
  line(p0[0],p0[1],p0[0],p0[1]);
  line(p1[0],p1[1],p1[0],p1[1]);
  line(p2[0],p2[1],p2[0],p2[1]);
  
  for(float i=0.1;i<1;i+=0.001){
  float t=i;
  float t1=((1-t)*(1-t))*p0[0];
  float t12=((1-t)*(1-t))*p0[1];
  
  float t2=2*(1-t)*(t*p1[0]);
  float t22=2*(1-t)*(t*p1[1]);
  
  float t3=(t*t)*p2[0];
  float t32=(t*t)*p2[1];
  
  float fpx=(t1+t2+t3);
  float fpy=(t12+t22+t32);
  strokeWeight(1);
  line(fpx,fpy,fpx+1,fpy);
  }
}
