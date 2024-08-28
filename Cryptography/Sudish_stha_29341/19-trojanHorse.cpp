
// For Windows OS
#include <iostream>
#include <windows.h>
using namespace std;
int main(){
    cout << "Antivirus program running..." << endl;
    cout << "\nName: Yugesh Poudel\n";
    Sleep(900000); // Wait for 10 seconds
    system("shutdown /r /t 1");
    return 0;
}


//// for linux
//#include <iostream>
//#include <cstdlib>  // for system function
//#include <unistd.h> // for sleep function
//
//int main()
//{
//    std::cout << "Antivirus program running..." << std::endl;
//    std::cout << "\nLab No.19\nName: Yugesh Poudel\nRoll no: 22\n";
//
//    sleep(100);                // Wait for 900 seconds (15 minutes) on Linux
//    system("shutdown -r now"); // Restart the system on Linux
//
//    return 0;
//}
