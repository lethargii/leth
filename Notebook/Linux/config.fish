if status is-interactive
    # Commands to run in interactive sessions can go here
end
if [ -d "/home/lethargii/.local/share/flatpak/exports/bin/" ] ;
  set PATH "/home/lethargii/.local/share/flatpak/exports/bin/:$PATH"
end
alias vim=io.neovim.nvim
