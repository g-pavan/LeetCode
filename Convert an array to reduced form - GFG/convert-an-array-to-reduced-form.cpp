//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	// Converts arr[0..n-1] to reduced form.
	void convert(int arr[], int n) {
	    // code here
	    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	    
	    for(int i=0; i<n; i++){
	        pq.push({arr[i],i});
	    }
	    
	    int i=0;
	    while(!pq.empty()){
	        arr[pq.top().second] = i;
	        i += 1;
	        pq.pop();
	    }

	}

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        ob.convert(arr, n);
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends