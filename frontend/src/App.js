import React, { Component } from 'react';
import logo from './logo.svg';
import style from './App.module.scss';

// fetch('/notifications/')

class App extends Component {
  render() {
    return (
      <div className={style.App}>
        <header className={style.appHeader}>
          <img src={logo} className={style.appLogo} alt="logo" />
          <p>
            Whatever
          </p>
          <a
            className={style.appLink}
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
