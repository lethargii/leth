local vim = vim
local Plug = vim.fn['plug#']

vim.call('plug#begin')

Plug ('nvim-treesitter/nvim-treesitter', { ['do'] = ':TSUpdate' })

Plug ('L3MON4D3/LuaSnip')

Plug ('williamboman/mason.nvim')
Plug ('williamboman/mason-lspconfig.nvim')
Plug ('neovim/nvim-lspconfig')
Plug ('hrsh7th/nvim-cmp')
Plug ('hrsh7th/cmp-nvim-lsp')
Plug ('hrsh7th/cmp-nvim-lsp-signature-help')
Plug ('hrsh7th/cmp-buffer')
Plug ('hrsh7th/cmp-path')
Plug ('saadparwaiz1/cmp_luasnip')

Plug ('rafamadriz/friendly-snippets')

Plug ('folke/tokyonight.nvim')

Plug ('windwp/nvim-autopairs')

Plug ('nvim-tree/nvim-web-devicons')
Plug ('nvim-tree/nvim-tree.lua')

Plug ('euclio/vim-markdown-composer', { ['do'] = function()
	vim.cmd('!cargo build --release --locked')
end})

Plug ('dhruvasagar/vim-table-mode')
vim.call('plug#end')

-- Mason - Language Server Protocol -------------------------------------------

require("mason").setup()
require("mason-lspconfig").setup()

require("mason-lspconfig").setup_handlers {
	function (server_name)
		require("lspconfig")[server_name].setup {}
	end,
	["java_language_server"] = function ()
		require("lspconfig")["java_language_server"].setup {
			handlers = {
				['client/registerCapability'] = function(err, result, ctx, config)
					local registration = {
						registrations = { result },
					}
					return vim.lsp.handlers['client/registerCapability'](err, registration, ctx, config)
				end
			},
		}
	end,
	["pylsp"] = function ()
		require("lspconfig").pylsp.setup {
			capabilities = require("cmp_nvim_lsp").default_capabilities(vim.lsp.protocol.make_client_capabilities()),
			settings = {
				pylsp = {
					plugins = {
						jedi_completion = {
							include_params = true,
						},
						pycodestyle = {
							maxLineLength = 120,
						},
					},
				},
			},
		}
	end
}

-- Treesitter - Highlighting --------------------------------------------------

require("nvim-treesitter.configs").setup{
	ensure_installed="all",
	highlight={
		enable=true,
		additional_vim_regex_highlighting=true
	},
	indent={enable=true}
}

-- Luasnip ---------------------------------------------------------------------

local luasnip = require("luasnip")
luasnip.setup()
require("luasnip.loaders.from_lua").lazy_load()
require("luasnip.loaders.from_vscode").lazy_load()

local has_words_before = function()
	local line, col = unpack(vim.api.nvim_win_get_cursor(0))
	return col ~= 0 and vim.api.nvim_buf_get_lines(0, line - 1, line, true)[1]:sub(col, col):match("%s") == nil
end

-- CMP - Autocompletion --------------------------------------------------------
local cmp = require 'cmp'
cmp.setup {
	snippet = {
		expand = function(args)
			require('luasnip').lsp_expand(args.body)
		end,
	},
	mapping = {
		["<Tab>"] = cmp.mapping(function(fallback)
			if cmp.visible() then
				cmp.select_next_item()
			elseif luasnip.expand_or_jumpable() then
				luasnip.expand_or_jump()
			elseif has_words_before() then
				cmp.complete()
			else
				fallback()
			end
		end, { "i", "s" }),

		["<S-Tab>"] = cmp.mapping(function(fallback)
			if cmp.visible() then
				cmp.select_prev_item()
			elseif luasnip.jumpable(-1) then
				luasnip.jump(-1)
			else
				fallback()
			end
		end, { "i", "s" }),
	},
	sources = {
		{ name = 'nvim_lsp' },
		{ name = 'nvim_lsp_signature_help' },
		{ name = 'luasnip' },
		{ name = 'buffer' },
		{ name = 'path' }
	},
}

-- Autopairs -----------------------------------------------------------------

require("nvim-autopairs").setup{}

-- Display numbers -----------------------------------------------------------

vim.wo.number = true

-- Theme ---------------------------------------------------------------------

vim.cmd[[colorscheme tokyonight]]

-- Tree - File Explorer ------------------------------------------------------

vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

vim.opt.termguicolors = true

require("nvim-tree").setup()

-- Markdown - Preview --------------------------------------------------------

vim.g.markdown_composer_external_renderer = 'flatpak-spawn --host pandoc --pdf-engine=xelatex -f markdown -t html'

-- Vim table mode ------------------------------------------------------------

vim.g.table_mode_corner='|'
