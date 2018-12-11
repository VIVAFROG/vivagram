import React, { Component } from 'react';
import styles from './App.module.scss';

// fetch('/notifications/')

class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <header className={styles.appHeader}>
          <h1 className={styles.appTitle}>Welcome to React</h1>
        </header>
        <p className={styles.appIntro}>To get started, whatever</p>
      </div>
    );
  }
}

export default App;
