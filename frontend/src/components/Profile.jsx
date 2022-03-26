import React from "react";
import Blockies from "react-blockies";
import ProfileMenu from "./ProfileMenu";

const Profile = ({ username, className }) => {
  return (
    <div className={className}>
      <div className="flex items-center justify-center gap-3">
        <h2 className="font-light text-lg">Hello, {username}!</h2>
        <ProfileMenu
          control={
            <button>
              <Blockies
                seed={username}
                size={12}
                scale={3}
                // color="#dfe"
                // bgColor="#ffe"
                // spotColor="#abc"
                className="rounded-full select-none"
              />
            </button>
          }
        />
      </div>
    </div>
  );
};

export default Profile;
