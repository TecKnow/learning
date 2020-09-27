import React from "react";
import ReactDom from "react-dom";
import "./index.css";
import moment from "moment";

function Tweet({ tweet }) {
  return (
    <div className="tweet">
      <Avatar hash={tweet.gravatar} />
      <div className="content">
        <NameWithHandle author={tweet.author} />
        <Time time={tweet.timestamp} />
        <Message text={tweet.message} />
        <div className="buttons">
          <LikeButton count={tweet.likes} />
          <CommentButton />
          <ShareButton />
          <RetweetButton count={tweet.retweets} />
        </div>
      </div>
    </div>
  );
}

function Avatar({ hash }) {
  let url = `https://www.gravatar.com/avatar/${hash}`;
  return <img src={url} className="avatar" alt="avatar" />;
}

function Message({ text }) {
  return <div>{text}</div>;
}

function NameWithHandle({ author }) {
  const { name, handle } = author;
  return (
    <span className="name-with-handle">
      <span className="name">{name}</span>
      <span className="handle">@{handle}</span>
    </span>
  );
}

const Time = ({ time }) => {
  const timeString = moment(time).fromNow();
  return <span className="time">{timeString}</span>;
};

const LikeButton = ({count}) => (<span className="like-button"><i className="fa fa-heart like-button" />{count> 0 && <span className="like-count">{count}</span>}</span>);

const CommentButton = () => <i className="far fa-comment" />;

function getRetweetCount(count) {
  if (count > 0) {
    return <span className="retweet-count">count</span>;
  } else {
    return null;
  }
}

const RetweetButton = ({ count }) => (
  <span className="retweet-button">
    <i className="fa fa-retweet retweet-button" />
    {getRetweetCount(count)}
  </span>
);

const ShareButton = () => <i className="fa fa-external-link-alt" />;

let testTweet = {
  message: "Something about cats.",
  gravatar: "xyz",
  author: {
    handle: "catperson",
    name: "MorganWebpaerson",
  },
  likes: 2,
  retweets: 0,
  timestamp: "2019-09-25 21:23:37",
};

ReactDom.render(<Tweet tweet={testTweet} />, document.querySelector("#root"));
