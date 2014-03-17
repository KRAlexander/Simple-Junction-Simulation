//#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>
#include <iostream>
using namespace std;
//#include "libxl.h" //Needed for excel output of data!!
#include <windows.h>
//using namespace libxl; // Needed for excel output of data!!
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream
#include <iostream>
#include <fstream>


/* Vector building blocks to use:
vector<vector<int>> mdVector;

	int tempValue;

		cout << "Enter an integer " << endl;
		cin >> tempValue;

		
		mdVector.push_back( vector<int>(2,0) );
		mdVector.back().at(0)=tempValue;
		mdVector.back().at(1)=(tempValue-5);
		cout << endl << "Integer entered: ";
		cout << mdVector.at(0).at(0) << "\t" << mdVector.at(0).at(1) << endl;
		*/
bool distance_is_decreasing_2cars(vector<vector<float>> Car, int Carnumber1, int Carnumber2);
float previous_distance_between_2cars (vector<vector<float>> Car, int Carnumber1, int Carnumber2);
float current_distance_between_2cars (vector<vector<float>> Car, int Carnumber1, int Carnumber2);
int generate_exit_x (int exitnumber);
bool car_allowed_to_move(vector<vector<float>> Car, int carnumber, int maximum_allowed_distance);//Evaluate if car is allowed to move in order to avert collision!!
int number_of_cars_passed=0;

vector<vector<int>> create_template_path_start_and_exit_number(int Startnumber, int exitnumber)
{
vector<vector<int>> templatepath;
int Startx;
int newx;
int exitnumberx;

if(Startnumber==0)
	Startx=550;
if(Startnumber==1)
	Startx=393;
if(Startnumber==2)
	Startx=236;
if(Startnumber==3)
	Startx=79;

//Start of path creation - decrease in y for constant x until y=0
templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=Startx;
		templatepath.back().at(1)=287;
for(int i=1; i!=-1;i++)
{	

	templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=Startx;
		templatepath.back().at(1)=287-i;
	//cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(i==287)	
		break;
}


//Path creation for different exitnumbers
if(exitnumber==0)
{
	exitnumberx=550;
	for(int i=0; i!=-1;i++)
{	
	newx=Startx-1-i;
	if(newx==0)
	{
	newx=628;
	Startx=628;
	i=0;
	}
	templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=newx;
		templatepath.back().at(1)=0;
	//cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(templatepath.back().at(0)==exitnumberx)
		{break;}
}

}
if(exitnumber==1)
{
	exitnumberx=393;
	for(int i=0; i!=-1;i++)
{	
	newx=Startx-1-i;
	if(newx==0)
	{
	newx=628;
	Startx=628;
	i=0;
	}
	templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=newx;
		templatepath.back().at(1)=0;
//	cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(templatepath.back().at(0)==exitnumberx)
		{break;}
}
	
}
if(exitnumber==2)
{
	exitnumberx=236;
	for(int i=0; i!=-1;i++)
{	
	newx=Startx-1-i;
	if(newx==0)
	{
	newx=628;
	Startx=628;
	i=0;
	}
	templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=newx;
		templatepath.back().at(1)=0;
//	cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(templatepath.back().at(0)==exitnumberx)
		{break;}
}
		
}
if(exitnumber==3)
{
	exitnumberx=79;
	for(int i=0; i!=-1;i++)
{	
	newx=Startx-1-i;
	if(newx==0)
	{
	newx=628;
	Startx=628;
	i=0;
	}
	templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=newx;
		templatepath.back().at(1)=0;
//	cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(templatepath.back().at(0)==exitnumberx)
		{break;}
}
		
}

		for(int i=0; i!=-1;i++)
{	
		templatepath.push_back( vector<int>(2,0) );
		templatepath.back().at(0)=exitnumberx;
		templatepath.back().at(1)=1+i;
	//cout << templatepath.back().at(0) << "," << templatepath.back().at(1) << endl;
	if(templatepath.back().at(1)==287)
		break;
}
		/* Output of created path
for(int index=0; index<templatepath.size(); index++)//Searching through all available path points
	{
	cout <<	 (templatepath.at(index).at(0)) << ", " << (templatepath.at(index).at(1)) << endl;
}

system("Pause");
*/
return templatepath;
}



int generate_exitnumber(int startnumber, bool rush_hour)
{
int exitnumber;
int tem;
if (rush_hour == false)
{
	if (startnumber == 0)//Exits 1,2,3 available
	{
		exitnumber = (rand() % 3) + 1;//Generates values: 1,2,3
		return exitnumber;
	}
	if (startnumber == 1)//Exits 2,3,0 available
	{
		exitnumber = (rand() % 3) + 2;// Generates values: 2,3,4
		if (exitnumber == 4)
		{
			exitnumber = 0;//Exitnumber created now: 0,2,3
			return exitnumber;
		}
		else
		{
			return exitnumber;
		}
	}
	if (startnumber == 2)//Exits 3,0,1 available
	{
		exitnumber = (rand() % 3) + 3;// Generates values: 3,4,5
		if (exitnumber > 3)
		{
			exitnumber = exitnumber - 4;//Exitnumbers generated now: 3,0,1
			return exitnumber;
		}
	}
	if (startnumber == 3)//Exits 0,1,2 available
	{
		exitnumber = (rand() % 3);// Generates values: 0,1,2
		return exitnumber;
	}
}

if (rush_hour == true)
{
	int exitnumber = 0;
	if (startnumber == 1)//This is not involved in the rush hour axis (0,2), therefore unaffected
	{
		exitnumber = (rand() % 3) + 2;// Generates values: 2,3,4
		if (exitnumber == 4)
		{
			exitnumber = 0;//Exitnumber created now: 0,2,3
			return exitnumber;
		}
		else
		{
			return exitnumber;
		}
	}
	if (startnumber == 3)//Exits 0,1,2 available
	{
		exitnumber = (rand() % 3);// Generates values: 0,1,2
		return exitnumber;
	}
	if (startnumber == 0)// 80% chance of it continuing on towards exit number 2 during rush hour
	{
		tem = (rand() % 10);
		if (tem == 0)
		{
			exitnumber = 1;
			return exitnumber;
		}
		if (tem == 1)
		{
			exitnumber = 3;
			return exitnumber;
		}
		else
		{
			exitnumber = 2; // 80 % chance
			return exitnumber;
		}
	}
	if (startnumber == 2)//Exits 3,0,1 available
	{
		exitnumber = (rand() % 3) + 3;// Generates values: 3,4,5
		if (exitnumber > 3)
		{
			exitnumber = exitnumber - 4;//Exitnumbers generated now: 3,0,1
		}
		return exitnumber;
	}
}
}



vector<vector<float>> initialise_Car(vector<vector<float>> Car, int carnumber, int global_t, bool rush_hour)
{
//Variable declarations
//vector<vector<float>> Car;
int startnumber;
int exitnumber;
float t=0.0;// Simulation time, measured in 0.1 s intervals, therefore t=10 s -> real-time = 1 s
int cx;//current x
int cy;//current y
//int px;//previous x
//int py;//previous y
float v=6;//velocity of car in pixels per 0.1 s (the current precision of animation)
/*
Create and initialise new car with carnumber and exitnumber, initial coordinates, ghost previous coordinates, etc.
1 : Assign car number (0-> infinity)
2 : assign startnumber randomly (0-3)
3 : assign exitnumber randomly based on startnumber
4 : set starting coordinates based on startnumber
Real speed of car to model = 28.8 km/h which equates to 80 pixels per second
*/

//Keeg startnumber fixed -> fixed starting co-ordinates for testing
if (rush_hour == false)
{
	startnumber = rand() % 4; //output: 0,1,2,3
}
if (rush_hour == true)
{
	int tem = (rand() % 15); //output: from 0 -> 14
	if (tem == 0)
	{
		startnumber = 2;
	}
	if (tem == 1)
	{
		startnumber = 1;
	}
	if (tem == 2)
	{
		startnumber = 3;
	}
	else if (tem!=0 && tem!=1 && tem!=2)
	{
		startnumber = 0;
	}
}


if(startnumber==0)
	cx=550;
if(startnumber==1)
	cx=393;
if(startnumber==2)
	cx=236;
if(startnumber==3)
	cx=79;
	
cy=278;//y of entry point always 287 pixels -
//!! To prevent nonsense output for firstnext position calculation, this is REDUCED FROM 287 TO 287-8=279-1 for x varience = 278 pixels

//Random generation of exitnumbers
//Keep fixed for testing

exitnumber=generate_exitnumber(startnumber, rush_hour);

//Creation of "Car" vector with 9 variables to identify car number and provide info to current and previous status
Car.push_back(vector<float>(9,0));
Car.back().at(0)=carnumber;
Car.back().at(1)=startnumber;
Car.back().at(2)=exitnumber;
Car.back().at(3)=global_t;
Car.back().at(4)=cx;
Car.back().at(5)=cy;
//Define previous co-ordinates
// When INITIALISING set px=cx, py=cy-v
Car.back().at(6)=cx;//px
Car.back().at(7)=cy+v;//py - in the beginning, car only changes direction in y direction
Car.back().at(8) = 0; // 0 when car is NOT at end position, 1 when it is
//cout << "Statistics for Car: " << Car.back().at(0) << ","  << Car.back().at(4)<< ","  << Car.back().at(5)<< endl;
return Car;
}

int change_x[17];
int change_y1 [17];// positive changes in y
int change_y2 [17];// negative change in y
int v=6; //Velocity in pixels per 0.1 s
int pow_v_2=(pow(v,2));
int temp;
void generate_changes_in_x_and_y1_and_y2()
{

	for(int n=0; n<17;n++)
	{
		change_x[n]= ((-1)*(8-n));
		temp=((pow_v_2)-(pow((change_x[n]),2)));
		change_y1 [n]=sqrt(temp);
		change_y2 [n]=sqrt(temp)*(-1);
	}


}

vector<vector<int>>path01;
vector<vector<int>>path02;
vector<vector<int>>path03;
vector<vector<int>>path10;
vector<vector<int>>path12;
vector<vector<int>>path13;
vector<vector<int>>path20;
vector<vector<int>>path21;
vector<vector<int>>path23;
vector<vector<int>>path30;
vector<vector<int>>path31;
vector<vector<int>>path32;

void initialise_paths()
{
		
			{path01=create_template_path_start_and_exit_number(0,1);}
			{path02=create_template_path_start_and_exit_number(0,2);}
			{path03=create_template_path_start_and_exit_number(0,3);}
		
			{path10=create_template_path_start_and_exit_number(1,0);}
			{path12=create_template_path_start_and_exit_number(1,2);}
			{path13=create_template_path_start_and_exit_number(1,3);}

			{path20=create_template_path_start_and_exit_number(2,0);}
			{path21=create_template_path_start_and_exit_number(2,1);}
			{path23=create_template_path_start_and_exit_number(2,3);}
		
			{path30=create_template_path_start_and_exit_number(3,0);}
			{path31=create_template_path_start_and_exit_number(3,1);}
			{path32=create_template_path_start_and_exit_number(3,2);}

}

vector<vector<int>> get_path(int startnumber,int exitnumber)
{
	vector<vector<int>> path;
	
		if(startnumber==0)
		{
			if(exitnumber==1)
			{path=path01;}
			if(exitnumber==2)
			{path=path02;}
			if(exitnumber==3)
			{path=path03;}
		}
		if(startnumber==1)
		{
			if(exitnumber==0)
			{path=path10;}
			if(exitnumber==2)
			{path=path12;}
			if(exitnumber==3)
			{path=path13;}
		}
		if(startnumber==2)
		{
			if(exitnumber==0)
			{path=path20;}
			if(exitnumber==1)
			{path=path21;}
			if(exitnumber==3)
			{path=path23;}
		}
		if(startnumber==3)
		{
			if(exitnumber==0)
			{path=path30;}
			if(exitnumber==1)
			{path=path31;}
			if(exitnumber==2)
			{path=path32;}
		}
	return path;
}

vector<vector<float>> next_coordinate_new(vector<vector<float>> Car, int carnumber)
{
	//int nx;//new x
//int ny;//new y
int nc [34] [2]; //new coordinates


float v=6;//velocity of car in pixels per 0.1 s (the current precision of animation)
//int loop;
int temp;
int posssible_co [2] [2]; //Two sets of POSSIBLE new Co-Ordinates
//vector<vector<float>> Car;
int startnumber;
//int carnumber;
int exitnumber;
float t;// Simulation time, measured in 0.1 s intervals, therefore t=10 s -> real-time = 1 s
int cx;//current x
int cy;//current y
int px;//previous x
int py;//previous y
int possible_cx;
int possible_cy;
int car_at_end;
//Assign values from input vector "Car" with 8 variables (listed and assigned below)


startnumber=	Car.at(carnumber).at(1);
exitnumber=		Car.at(carnumber).at(2);
t=				Car.at(carnumber).at(3);
cx=				Car.at(carnumber).at(4);
cy=				Car.at(carnumber).at(5);
px=				Car.at(carnumber).at(6);//=cx;//px
py=				Car.at(carnumber).at(7);//=cy-v;//py
//car_at_end =    Car.at(carnumber).at(8);
if((cx==generate_exit_x(exitnumber)) && (cy>270))
{
	return Car;
}
//Grab the path from the path creator, show the number of co-ordinates in the chosen path

vector<vector<int>> path;
path=get_path(startnumber,exitnumber);

//time updates by +0.1 seconds
Car.at(carnumber).at(3)=t+0.1;
if((car_allowed_to_move(Car, carnumber, 35))==true)//Determining if car is allowed to move!!
{
for(int n=0; n<path.size(); n++)
{
	if((cx==path.at(n).at(0)) && (cy==path.at(n).at(1)))
	{
		//Update Car properties if car is allowed to move
		//Update past co-ordinates
		Car.at(carnumber).at(6)=cx;//px
		Car.at(carnumber).at(7)=cy;//py
		//Update future co-ordinates
		Car.at(carnumber).at(4)=path.at((n+8)).at(0);
		Car.at(carnumber).at(5)=path.at((n+8)).at(1);
		n=path.size();	
	}
}
}

if(cx==generate_exit_x(Car.at(carnumber).at(2)))
{
	if(Car.at(carnumber).at(5)>271)
	{
		Car.at(carnumber).at(8) = 1; // Car is now officially at end position!!
		number_of_cars_passed++;
	}
}
//cout << "Next x,y coordinate: " << cx << ", " << cy << endl;
return Car;
}


bool car_allowed_to_move(vector<vector<float>> Car, int carnumber, int maximum_allowed_distance)//Evaluate if car is allowed to move in order to avert collision!!
{
bool allowed_to_move=true;

if((Car.at(carnumber).at(4)-Car.at(carnumber).at(6)<0) || (Car.at(carnumber).at(5)-Car.at(carnumber).at(7)>0))
{
	return allowed_to_move = true;
}

for (int carnumber_index = 0; carnumber_index < Car.size(); carnumber_index++)
{
	if (Car.at(carnumber_index).at(8) == 0)//Only if car is not at end position!!
	{
		if (carnumber_index != carnumber)
		{
			if (Car.at(carnumber_index).at(5) == 0)//If other car is in roundabout, ie. at cy==0
			{
				if (current_distance_between_2cars(Car, carnumber, carnumber_index) < maximum_allowed_distance) //If the distance between the approaching cars is less than maximum allowed distance
				{
					//if(distance_is_decreasing_2cars(Car, carnumber, carnumber_index))
					{
						return allowed_to_move = false;
					}
				}

			}
		}
	}
}
return allowed_to_move;
}


int generate_exit_x (int exitnumber)
{
int exitnumberx;
//Path creation for different exitnumbers
if(exitnumber==0)
{
	exitnumberx=550;
}
if(exitnumber==1)
{
	exitnumberx=393;	
}
if(exitnumber==2)
{
	exitnumberx=236;		
}
if(exitnumber==3)
{
	exitnumberx=79;
}
return exitnumberx;
}

int convert_global_t_float_to_global_t_int(float time)
{
	int global_time_f= (int((time)*10));
	return global_time_f;
}
float convert_global_t_int_to_global_t_float(int time)
{
	float global_time_f= (float(time) /10);
	return global_time_f;
}
int convert_simulation_time_float_to_simulation_time_int(float simulation_time_float)
{
	int simulation_time_int= (int((simulation_time_float)*10));
	return simulation_time_int;
}

bool whole_number(int rate_of_car_creation_int, int global_time_int, int simulation_time_int)
{
	//create list of n x rate of car creation, with limit of n x rate = simulation time/10
//float global_time_float = convert_global_t_int_to_global_t_float(global_time_int);
//float simulation_time_float = convert_global_t_int_to_global_t_float(simulation_time_int);
//vector<int> list;

for(float n=0.0; (n*rate_of_car_creation_int)<(simulation_time_int) ; n=n+1.0)
{
//list.push_back((n*rate_of_car_creation_int));
if(global_time_int==(n*rate_of_car_creation_int))
{
return true;
}
}
return false;
}

float current_distance_between_2cars (vector<vector<float>> Car, int Carnumber1, int Carnumber2)
{
float distance;
int carnumber=Carnumber1;
float cx1=	Car.at(carnumber).at(4);//Current X
float cy1=	Car.at(carnumber).at(5);//Current Y
carnumber=Carnumber2;
float cx2=	Car.at(carnumber).at(4);//Current X
float cy2=	Car.at(carnumber).at(5);//Current Y

float diff_x_2=pow((cx1-cx2),2);
//cout << diff_x_2 << endl;
float diff_y_2=pow((cy1-cy2),2);
distance=sqrt(diff_x_2+diff_y_2);

return distance;
}
float previous_distance_between_2cars (vector<vector<float>> Car, int Carnumber1, int Carnumber2)
{
float distance;
int carnumber=Carnumber1;
float px1=	Car.at(carnumber).at(6);//Previous X
float py1=	Car.at(carnumber).at(7);//Previous Y
carnumber=Carnumber2;
float px2=	Car.at(carnumber).at(6);//Previous X
float py2=	Car.at(carnumber).at(7);//Previous Y

float diff_x_2=pow((px1-px2),2);
//cout << diff_x_2 << endl;
float diff_y_2=pow((py1-py2),2);
distance=sqrt(diff_x_2+diff_y_2);

return distance;
}
bool distance_is_decreasing_2cars(vector<vector<float>> Car, int Carnumber1, int Carnumber2)
{
	if((current_distance_between_2cars(Car, Carnumber1, Carnumber2)-previous_distance_between_2cars(Car, Carnumber1, Carnumber2))<0)
	{return true;}
	else
	{return false;}

}

string convert_Int(int number)
{
	stringstream ss;
	ss << number;
	return ss.str();
}




int main ()
{

	bool show_mode;
	bool exit = false;
	int tem;
	while (exit == false)
	{
		cout << "Show mode (0) or Analytical Mode(1)?" << endl;
		cin >> tem;
		if (tem == 0)
		{
			show_mode = true;
			exit = true;
		}
		else if (tem == 1)
		{
			show_mode = false;
			exit = true;
		}
		else
		{
			cout << "Invalid Input - Please Repeat" << endl;
		}
	}

bool rush_hour;
exit = false;
while (exit == false)
{
		cout << "Rush Hour? (1/0)" << endl;
		cin >> tem;
		if (tem == 1)
		{
			rush_hour = true;
			exit = true;
		}
		else if (tem == 0)
		{
			rush_hour = false;
			exit = true;
		}
		else
		{
			cout << "Invalid Input - Please Repeat" << endl;
		}
}



if(show_mode==true)
{
/*
10 pixels per meter
to model speed of 28.8 km/h (8 m/s), speed of 80 pixels per second needed
*/
srand(time(NULL));//randomise list of pseudo-random numbers

float v=6;//velocity of car in pixels per 0.1 s (the current precision of animation)
//int loop;
//int temp;
//int pc [2] [2]; //Two sets of POSSIBLE new Co-Ordinates
vector<vector<float>> Car;
int startnumber;
int carnumber=0;//Set carnumber to 0 for initial car initialisation
int exitnumber;
float t=0.0;// Simulation time, measured in 0.1 s intervals, therefore t=10 s -> real-time = 1 s
//float global_t=0.0;
int cx;//current x
int cy;//current y
int px;//previous x
int py;//previous y
float simulation_time_float;
float simulation_time_int;//simulation time x10 to be used at int values
float rate_car_creation;
//Setup initialising variables

generate_changes_in_x_and_y1_and_y2();
initialise_paths();
ofstream file;
cout << "Enter Simulation Time (s)" << endl;
cin >> simulation_time_float;
simulation_time_int=convert_simulation_time_float_to_simulation_time_int(simulation_time_float);
cout << "Enter Rate of Car Creation (seconds per car)" << endl;
cin >> rate_car_creation;
//cout << "Rate of Car Creation entered: " << rate_car_creation << endl;
//system("Pause");
int rate_car_creation_int= convert_global_t_float_to_global_t_int(rate_car_creation);
//cout << "Rate of Car Creation entered: " << rate_car_creation_int << endl;
//system("Pause");


float global_t_float=0.0;  
int global_t_int=convert_global_t_float_to_global_t_int(global_t_float);


/* //Excel Stuff!!
//sheet->writeNum(y, x, value);
// sheet->writeStr(2, 1, L"Hello, World !");


sheet->writeStr(1,0,L"Global Time in Simulation ");
sheet->writeStr(1,1,L"Number of Cars in the System" );
sheet->writeStr(1,2,L"Car Co-Ordinates" );
*/
file.open("simulation_roundabout.txt", ios::ate | ios::in | ios::app);
file << "Simulation Time (s): " << endl << simulation_time_float << endl;
file << "Rate of Car Creation: " << endl << rate_car_creation << endl;
//file.close();

while(global_t_float<simulation_time_float)
{
	cout.setf(ios::fixed, ios::floatfield);
    cout.setf(ios::showpoint);
	//cout << "Time is (float): " << global_t_float << endl;
	cout << global_t_float << endl;
//	cout << "Time is int: " << global_t_int << endl;
	//cout << "Total Simulation time is (float): " << simulation_time_float << endl;
//	cout << "Total Simulation time is int: " << simulation_time_int << endl;

//		sheet->writeNum((global_t_int+2), 0, global_t_float);




//Initialise new car, if the global time is a multiple of the rate of car creation, ie. if division of time by rate gives a whole number!
if(whole_number(rate_car_creation_int, global_t_int , simulation_time_int )==true)//if true, create new car
{
Car=Car=initialise_Car(Car,carnumber, global_t_float, rush_hour);//Returns vector "Car" with 8 variables (listed and assigned below)
carnumber=		Car.at(carnumber).at(0);
startnumber=	Car.at(carnumber).at(1);
exitnumber=		Car.at(carnumber).at(2);
t=				Car.at(carnumber).at(3);
cx=				Car.at(carnumber).at(4);//Current X
cy=				Car.at(carnumber).at(5);//Current Y
px=				Car.at(carnumber).at(6);//=cx;//px
py=				Car.at(carnumber).at(7);//=cy-v;//py
				//Car.at(carnumber).at(8);//If 0 car not at end position, if 1 car IS at end
carnumber=carnumber+1;//Increase carnumber for next car initialisation
}

//cout << "number of cars in system: " << Car.size() << endl;
//cout << "coordinates of Car 0: " << Car.at(0).at(4) << "," << Car.at(0).at(5) << endl;
/*
cout << "list of all cars in system" << endl;
for(int n=0; n<Car.size(); n++)
{
cout << "Car Number: " << Car.at(n).at(0) << endl;
}
*/

int array[2][1000]={0};


//file.open("simulation.txt", ios::ate | ios::in | ios::app);
for(int n=0; n<900; n++)
{

if(n<Car.size())
{
	if (Car.at(n).at(8) == 0)
	{
		Car = next_coordinate_new(Car, n);
	}
//cout << "Car Number: " << Car.at(n).at(0) << " " << Car.at(n).at(4) << "," << Car.at(n).at(5) << endl;
array[0][n]=Car.at(n).at(4);
array[1][n]=Car.at(n).at(5);
}
else
{
}
file << array[0][n] << endl << array[1][n] << endl;
}




global_t_int=global_t_int+1;
global_t_float=convert_global_t_int_to_global_t_float(global_t_int);

//cout << endl;

}
//} //Needed for spreadsheet generation!!
/*
	if(book->save(L"Math_Simulation.xls"))
	{
		::ShellExecute(NULL, L"open", L"Math_Simulation.xls", NULL, NULL, SW_SHOW);        
	}
	else
        {
            std::cout << book->errorMessage() << std::endl;
        }
	book->release();
	*/
//} // Needed for spreadsheet generation!!

	/*
	//Excel Spreadsheet generation
	 Book* book = xlCreateBook();
    if(book)
    {
        Sheet* sheet = book->addSheet(L"Sheet1");
        if(sheet)
        {
          // sheet->writeNum(y, x, value);
		  // sheet->writeStr(2, 1, L"Hello, World !");
          // sheet->writeFormula(6, 2, L"SUM(B5:B7)");
      for(int index=0; index<Car.size(); index++)
		{	
			   sheet->writeStr(2, 1, L"Data For Car: 0");
			if(Car.at(index).at(0)==0)
			{
				
				   sheet->writeNum(5, 1, Car.at(index).at(0));
				   sheet->writeNum(5, 2, Car.at(index).at(1));
				   sheet->writeNum(5, 3, Car.at(index).at(2));
				   sheet->writeNum(5, 4, Car.at(index).at(3));
				   sheet->writeNum(5, 5, Car.at(index).at(4));
				   sheet->writeNum(5, 6, Car.at(index).at(5));
				   sheet->writeNum(5, 7, Car.at(index).at(6));
				   sheet->writeNum(5, 8, Car.at(index).at(7));
			}
		}
        }
        if(book->save(L"Maths-Simulation.xls")) 
        {
            ::ShellExecute(NULL, L"open", L"Maths-Simulation.xls", NULL, NULL, SW_SHOW);        
        }
        else
        {
            std::cout << book->errorMessage() << std::endl;
        }
        book->release();		
    } 
	
	*/
	file.close();
	cout << "Animation time: " << simulation_time_float << endl;
	cout << "Number of cars passed: " << number_of_cars_passed << endl;
	system("Pause");
	return 0;
	}

else if(show_mode==false) //This is the analytical mode
{
/*
10 pixels per meter
to model speed of 28.8 km/h (8 m/s), speed of 80 pixels per second needed
*/

float v=8;//velocity of car in pixels per 0.1 s (the current precision of animation)
//int loop;
//int temp;
//int pc [2] [2]; //Two sets of POSSIBLE new Co-Ordinates
vector<vector<float>> Car;
int startnumber;
int carnumber=0;//Set carnumber to 0 for initial car initialisation
int exitnumber;
float t=0.0;// Simulation time, measured in 0.1 s intervals, therefore t=10 s -> real-time = 1 s
//float global_t=0.0;
int cx;//current x
int cy;//current y
int px;//previous x
int py;//previous y
float simulation_time_float;
float simulation_time_int;//simulation time x10 to be used at int values
float rate_car_creation;

int rep_time;
float average_seconds_per_repetition = 0;

initialise_paths();

ofstream file;
file.open("simulation_roundabout_analytical_output.txt", ios::ate | ios::in | ios::app);


int repetitions;
cout << "Enter Number of Repetitions" << endl;
cin >> repetitions;
cout << "Enter Simulation Time (s)" << endl;
cin >> simulation_time_float;
simulation_time_int=convert_simulation_time_float_to_simulation_time_int(simulation_time_float);
cout << "Enter Rate of Car Creation (seconds per car)" << endl;
cin >> rate_car_creation;
int rate_car_creation_int= convert_global_t_float_to_global_t_int(rate_car_creation);
int rep=0;

bool new_label;
bool exit = false;
int tem;
while (exit == false)
{
	cout << "Start a new label row? (0/1)" << endl;
	cin >> tem;
	if (tem == 1)
	{
		new_label = true;
		exit = true;
	}
	else if (tem == 0)
	{
		new_label = false;
		exit = true;
	}
	else
	{
		cout << "Invalid Input - Please Repeat" << endl;
	}
}
if (new_label == true)
{
	file << "simulation_time" << ", " << "Rate of Car creation" << ", " << "Number of cars created" << ", " << "number_of_cars_passed" << endl;
}
int time0 = int(time(0));//Time at start of simulation
while(rep<repetitions)
{
	int seconds_now = int(time(0));
cout << "Execution Number: " << rep << " ..." << endl;
Car.clear();
float global_t_float=0.0;  
int global_t_int=convert_global_t_float_to_global_t_int(global_t_float);
carnumber=0;
srand(time(NULL));//randomise list of pseudo-random numbers
number_of_cars_passed=0;
while(global_t_float<simulation_time_float)
{
	cout.setf(ios::fixed, ios::floatfield);
    cout.setf(ios::showpoint);
	//cout << global_t_float << endl;

//Initialise new car, if the global time is a multiple of the rate of car creation, ie. if division of time by rate gives a whole number!
if(whole_number(rate_car_creation_int, global_t_int , simulation_time_int )==true)//if true, create new car
{
Car=Car=initialise_Car(Car,carnumber, global_t_float,rush_hour);//Returns vector "Car" with 8 variables (listed and assigned below)
carnumber=		Car.at(carnumber).at(0);
startnumber=	Car.at(carnumber).at(1);
exitnumber=		Car.at(carnumber).at(2);
t=				Car.at(carnumber).at(3);
cx=				Car.at(carnumber).at(4);//Current X
cy=				Car.at(carnumber).at(5);//Current Y
px=				Car.at(carnumber).at(6);//=cx;//px
py=				Car.at(carnumber).at(7);//=cy-v;//py
				//Car.at(carnumber).at(8);//If 0 car NOT at end position
carnumber=carnumber+1;//Increase carnumber for next car initialisation
}

for(int n=0; n<Car.size();n++)
{
	if (Car.at(n).at(8) == 0)
	{
		Car = next_coordinate_new(Car, n);
	}
}

global_t_int=global_t_int+1;
global_t_float=convert_global_t_int_to_global_t_float(global_t_int);
}

file << simulation_time_float << ", "<< rate_car_creation << ", " << Car.size() << ", " << number_of_cars_passed << endl;


if (rep == 0)
{
	rep_time = int(time(0)) - time0;
	average_seconds_per_repetition = rep_time;
}
else
{
	rep_time = int(time(0)) - time0;
	average_seconds_per_repetition = (float(rep_time) / (rep + 1));
}


rep=rep+1;

cout << "Average Number of Seconds Per Repetition: " << average_seconds_per_repetition << endl;
cout << "Projected Time to Completion (seconds): " << (((repetitions - rep)*average_seconds_per_repetition)) << endl;
cout << "Projected Time to Completion (minutes): " << (float(((repetitions - rep)*average_seconds_per_repetition)) / 60.0) << endl;

}

	file.close();
	cout << "Simulation has finished" << endl;
	system("Pause");
	return 0;
}
}


/*
time_t now = time(0);
time_t later = time(0);
int seconds_passed = int(later) - int(now);
float minutes_passed = float(seconds_passed) / 60.0;
*/