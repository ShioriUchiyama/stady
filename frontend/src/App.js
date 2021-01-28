import React from 'react';
import Auth from './components/Registration'; 
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { CookiesProvider, withCookies } from 'react-cookie';

function APP () {
    return (
        <Router>
            <div className="App">
                <CookiesProvider>
                    <Route path="/auth" component={Auth}></Route>
                </CookiesProvider>
            </div>
        </Router>
    );
}

export default withCookies(APP);
